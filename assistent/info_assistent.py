import pyrogram
 # это потом подругому сделаю
gender = "М"
gender_data = ""
if gender == "М":
    gender_data = "сэр"
else:
    gender_data = "мэм"

tg_contact = {
    # имя : tg ник
}

films_url = # url к фильмам
search_films_PATH = # путь к поисковой строке
button_search_PATH = # путь к кнопке поиска

sample = {
    # название : ссылка на ютуб
}

app = pyrogram.Client("my_bot", api_id=# id апи тг, api_hash= # id хэша в тг)
hot_answer = #любое сообщение при ответе можно оставить и так ""

new = [] # имена как в тг от кого будут приходить пуш уведомления
hot_word = [] # горячие слова из-за которых будут приходить пуш уведомления