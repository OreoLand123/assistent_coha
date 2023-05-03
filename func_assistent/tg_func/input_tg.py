from fuzzywuzzy import fuzz
from func_assistent.base_func import voice
from func_assistent.base_func.base import yes_and_no, command_no
from func_assistent.base_func.record_voice import voice_func
from assistent.info_assistent import tg_contact, app
from func_assistent.base_func.number import int_translate_text
from time import sleep

def input_tg_user(text):
    flag = False
    for contact in tg_contact:
        print(fuzz.partial_ratio(contact, text))
        if fuzz.partial_ratio(contact, text) >= 70:
            voice.speaker(f"Нашёл контакт {contact}")
            voice.speaker("процитируйте сообщение которое хотите написать")
            flag = True
            while flag:
                text = voice_func()
                status = command_no(text)
                if status:
                    voice.speaker("есть")
                    return
                voice.speaker(f"я правильно понимаю вы хотиите написать {text}")
                yes_no = voice_func()
                status = yes_and_no(yes_no)
                if status:
                    break
                elif status == False:
                    voice.speaker("хорошо сэр что вы хотите написать")
                    continue
                else:
                    voice.speaker("я вас не раслышал сэр повторите что хотите написать")
            contact_tg = tg_contact[contact]
            app.send_message(contact_tg, text)
    return flag

def gpt_input_tg(data):
    text = data.split()
    for sim in text:
        if fuzz.partial_ratio(sim, "скажи") >= 65 or fuzz.partial_ratio(sim, "сказать") >= 65:
            text = " ".join(text[text.index(sim) + 1:])
            break
    app.send_message("@dumebot", text)
    voice.speaker("обрабатываю информацию")
    sleep(2)
    while True:
        message = "Запрос выполняется…"
        message_stop = ""
        sleep(2)
        for mess in app.get_chat_history("@dumebot"):
            message_stop = mess.text
            break
        if message_stop != message:
            break
    for num in message_stop.split():
        if num.isdigit():
            firs_num = num
            next_num = int_translate_text(num)
            message_stop = message_stop.replace(firs_num, next_num, 1)
    if len(message_stop.split()) > 150:
        count_start = 0
        count_end = 0
        while True:
            if count_end > len(message_stop.split()):
                return
            count_end += 100
            utils_contain = " ".join([i for i in message_stop.split()[count_start:count_end]])
            voice.speaker(utils_contain)
            count_start += 100
    else:
        voice.speaker(message_stop)
        return
    return