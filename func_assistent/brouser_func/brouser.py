from fuzzywuzzy import fuzz
from func_assistent.base_func.base import command_no
from func_assistent.base_func.voice import speaker
from func_assistent.base_func.record_voice import voice_func
from assistent.info_assistent import films_url, gender_data, search_films_PATH, button_search_PATH, sample
import webbrowser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager



def open_brouser(url):
    url = url
    chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    webbrowser.register("chrome", None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get("chrome").open_new(url)

def films():
    open_brouser(films_url)
    speaker(f"Приятного просмотра {gender_data}")

def get_film(data):
    text = data.split()
    for sim in text:
        if fuzz.partial_ratio(sim, "сериал") >= 80 or fuzz.partial_ratio(sim, "фильм") >= 80:
            text = " ".join(text[text.index(sim) + 1:])
            break
    option = Options()
    option.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=option)
    driver.get(films_url)
    search = driver.find_element(By.XPATH, search_films_PATH)
    search.click()
    search.send_keys(text)
    driver.find_element(By.XPATH, button_search_PATH).click()
    speaker("Вот всё что было найдено")
    speaker("Приятного просмотра")

def youtube():
    open_brouser(url="https://www.youtube.com/")
    speaker("приятного отдыха")


def music():
    while True:
        text = voice_func()
        if command_no(text):
            speaker("хорошо сегодня без музыки")
            return
        speaker("ищу подходящий плейлист в ваших семплах")
        for samp in sample:
            if fuzz.partial_ratio(text, samp) >= 70:
                speaker("нашёл подходящий плейлист")
                speaker("запускаю")
                open_brouser(url=sample[samp])
                speaker("Приятного вам отдыха")
                return
        speaker("Не нашёл подходящего плейлиста по вашему запросу")
        speaker("повторите плейлист который вы хотите послушать")
