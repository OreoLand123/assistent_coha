from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from func_assistent.brouser_func.brouser import get_film, music, films
from func_assistent.tg_func.input_tg import input_tg_user, gpt_input_tg
import words
from func_assistent.base_func import voice
from fuzzywuzzy import fuzz




def recognize(data, vectorizer, clf):
    print(data)
    '''
    Анализ распознанной речи
    '''

    # проверяем есть ли имя бота в data, если нет, то return
    trg = words.TRIGGERS.intersection(data.split())
    if not trg:
        return
    if trg and fuzz.partial_ratio("напиши", data) >= 60:
        voice.speaker(f"уже пишу ")
        status = input_tg_user(data)
        print(data)
        if status:
            voice.speaker(f"сообщение отправлено")
        elif status == False:
            voice.speaker(f"контакт не найден")
        else:
            voice.speaker(f"Что то хотите")
        return

    elif trg and fuzz.partial_ratio(data, "фильм") >= 80 or fuzz.partial_ratio(data, "сериал") >= 80:
        voice.speaker(f"Уже ищу")
        get_film(data)
        return
    elif trg and fuzz.partial_ratio(data, "музончик") >= 70 or fuzz.partial_ratio(data, "музыка") >= 70:
        voice.speaker(f"открываю ваш сэмпл")
        voice.speaker(f"какой плейлист включить")
        music()
        return
    elif trg and fuzz.partial_ratio(data, "скажи") >=80 or fuzz.partial_ratio(data, "сказать")>= 80:
        gpt_input_tg(data)
        return
    # удаляем имя бота из текста
    data.replace(list(trg)[0], '')

    # получаем вектор полученного текста
    # сравниваем с вариантами, получая наиболее подходящий ответ
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]

    # получение имени функции из ответа из data_set
    func_name = answer.split()[0]

    # озвучка ответа из модели data_set
    voice.speaker(answer.replace(func_name, ''))
    exec(func_name + "()")


vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(list(words.data_set.keys()))
clf = LogisticRegression()
clf.fit(vectors, list(words.data_set.values()))
del words.data_set

