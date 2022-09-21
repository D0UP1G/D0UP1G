import webbrowser


def search():
    url = 'https://google.com'
    webbrowser.open(url, new=0, autoraise=True)
    return("Выполнено")
