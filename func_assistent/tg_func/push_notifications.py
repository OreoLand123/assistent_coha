from pyrogram import filters
from func_assistent.base_func. record_voice import voice_func
from func_assistent.base_func.voice import speaker
from func_assistent.base_func.base import yes_and_no
from func_assistent.base_func.record_voice import record_voice_tg
from assistent.info_assistent import hot_answer, app, hot_word, new
from time import sleep


@app.on_message(filters.private)
def handle_private_message(client, message):
    # Получить текст сообщения
    print(message)
    if any(word in message.chat.first_name for word in new) and message.from_user.id != 2023643840:
        if message.voice:
             file = app.download_media(message.voice.file_id, file_name="audio.mp3")
             sleep(2)
             print(file)
             if file:
                 text_speech = record_voice_tg(file)
                 text = text_speech
             else:
                 speaker("произошла ошибка в загрузке аудио файла который вам отправил пользователь")
        else:
            text = message.text.lower().split()
        print(text)
        for hot in hot_word:
            if hot in message.text.lower().split():
                speaker(f"у вас важное сообщение от контакта {message.chat.first_name}")
                speaker("хотите я вам зачитаю сообщение?")
                sleep(0.5)
                while True:
                    sleep(0.5)
                    data = voice_func()
                    status = yes_and_no(data)
                    if status:
                        speaker(message.text)
                        speaker("хотите ответить?")
                        sleep(0.5)
                        data = voice_func()
                        status = yes_and_no(data)
                        if status:
                            speaker("процитируйте своё сообщение")
                            sleep(0.5)
                            data = voice_func()
                            sleep(0.5)
                            speaker("отправила")
                            app.send_message(chat_id=message.from_user.id, text=hot_answer + data)
                            break
                        elif status == False:
                            speaker("хоршо")
                            break
                        else:
                            speaker("я не поняла что вы имели в виду поэтому ничего не отправила")
                            break
                    elif status == False:
                        speaker("хоршо больше не отвлекаю")
                        break
                    else:
                        speaker("я не расслышала повторите пожалуйста")
                break
