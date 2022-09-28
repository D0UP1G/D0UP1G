import webbrowser
import os
import subprocess
import pyautogui as pg


def google():
    url = 'https://google.com'
    webbrowser.open(url, new=0, autoraise=True)
    return("Выполнено")
def yandex():
    url = 'https://dzen.ru/'
    webbrowser.open(url, new=0, autoraise=True)
    return('Выполнено')
def OBS():
    if 1==1:
        pg.hotkey('win')
        pg.typewrite('OBS', 0.1)
        pg.press('enter', 1)
        return('выполнено')

def start_yandex():
    if 1==1:
        pg.hotkey('win')
        pg.typewrite('yandex', 0.01)
        pg.press('enter', 1)
