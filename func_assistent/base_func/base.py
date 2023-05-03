from fuzzywuzzy import fuzz
from func_assistent.base_func.voice import speaker
import os
import pyautogui
import win32api


def yes_and_no(data):
    yes = ["да", "верно", "вточку", "правильно", "прими", "подтверждаю"]
    no = ["нет", "отказано", "отмена", "неправильно", "не верно", "другое"]
    print(data)
    for y in yes:
        print(fuzz.partial_ratio(data, y))
        if fuzz.partial_ratio(data, y) >= 90:
            return True
    for n in no:
        print(fuzz.partial_ratio(data, n))
        if fuzz.partial_ratio(data, n) >= 90:
            return False
    return None

def command_no(data):
    command = ["отмена", "не хочу писать", "отмени", "назад"]
    for c in command:
        print(fuzz.partial_ratio(data, c))
        if fuzz.partial_ratio(data, c) >= 80:
            return True
    else:
        return False

def screen_shot():
    i = 1
    while True:
        if os.path.exists(fr"C:\Users\User\OneDrive\Рабочий стол\всё\cкриншоты\screenshot{i}.png"):
            i += 1
            continue
        pyautogui.screenshot(fr"C:\Users\User\OneDrive\Рабочий стол\всё\cкриншоты\screenshot{i}.png")
        break
    speaker("скриншот получен")


def language():
    klid = win32api.GetKeyboardLayout(0)
    print( klid & (2**16 - 1))
    if klid & (2**16 - 1) == 1033:
        print(1)
        win32api.LoadKeyboardLayout('00000419', 1)
    else:
        print(2)
        win32api.LoadKeyboardLayout('00000409', 1)