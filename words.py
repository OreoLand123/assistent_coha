from assistent.info_assistent import gender_data

TRIGGERS = {"коха", "кофа", "кока", "тока"}



data_set = {
    "привет":"dialog приветствую вас",
    "как у тебя дела":"dialog всё хорошо готов выполнять задачи",
    "чем занят":f"dialog жду ваших указаний {gender_data}",
    "спасибо":f"dialog рад помочь {gender_data}",
    "хорошая работа":f"dialog спасибо {gender_data}",
    "молодец":f"dialog знаю {gender_data}",
    "как дела":f"dialog всё в порядке",
    "кайф":f"dialog я знаю",
    "как тебе": "dialog это топ",


    "смени язык":f"language сменил {gender_data}",
    "язык":f"language уже сменил {gender_data}",

    "браузеров":f"web открыл {gender_data}",
    "браузер":f"web уже {gender_data}",

    "ютуб":f"youtube открываю {gender_data}",
    "ютюб":f"youtube секунду {gender_data}",
    "ютьюб":f"youtube хорошо {gender_data}",
    "юту":f"youtube открываю ютьюб",
    "ютубе":f"youtube открываю",


    "режим просмотра":"films открываю",
    "скриншот":"screen_shot сделал",







}