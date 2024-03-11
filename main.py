import pyautogui

new_app_title = ''

while True:
    app_title = pyautogui.getActiveWindowTitle()

    print(f'app_title = {app_title}, new_app_title = {new_app_title}')
    if app_title != new_app_title:
        if new_app_title == "Telegram Web - Google Chrome":
            pyautogui.hotkey('shift', 'alt')
            new_app_title = app_title
        new_app_title = ''
        if app_title == "Telegram Web - Google Chrome":
            pyautogui.hotkey('shift', 'alt')
            new_app_title = app_title
