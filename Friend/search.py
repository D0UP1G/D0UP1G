import webbrowser
import os
import main

def google():
    url = 'https://google.com'
    webbrowser.open(url, new=0, autoraise=True)
    return("Выполнено")
def yandex():
    url = 'https://dzen.ru/'
    webbrowser.open(url, new=0, autoraise=True)
    return('Выполнено')
def OBS():
    os.system('стрим.lnk')
