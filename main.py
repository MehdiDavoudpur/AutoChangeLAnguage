import tkinter as tk
import threading
import time
import pyautogui

# new_app_title is necessary for checking  if app title is changed or not.
new_app_title = ''
# title_list is necessary for checking being repetitive in a for loop to add to title_list_string.
title_list = []
# title_list_string is necessary for printing out to user.
title_list_string = ''


def background_task():
    while True:
        global new_app_title
        global title_list
        global title_list_string
        # get active app title as app_title.
        app_title = pyautogui.getActiveWindowTitle()
        # check if app title is changed or not.
        if app_title != new_app_title:
            # check if app title is changed from  "کافه اینترنشنال" to other thing. new app title here is previous
            # app title really.
            i = 0
            for title in title_list:
                if title == app_title:
                    i = 1
            if i == 0:
                # app title is not repetitious and is appended to title_list.
                title_list.append(app_title)
                if app_title:
                    title_list_string = title_list_string + app_title + '\n'
            # check if app title is changed from  "کافه اینترنشنال" to other thing. new app title here is previous
            # app title really.
            if "کافه اینترنشنال" in new_app_title:
                # change language from فا to ENG
                pyautogui.hotkey('shift', 'alt')
            # check if app title is changed from other thing to  "کافه اینترنشنال"
            if "کافه اینترنشنال" in app_title:
                # change language from ENG to فا
                pyautogui.hotkey('shift', 'alt')
            # refresh app title
            new_app_title = app_title

        time.sleep(0.5)


# Create a thread for the background task
background_thread = threading.Thread(target=background_task)
# Set the thread as a daemon, so it automatically terminates when the main program exits
background_thread.daemon = True
background_thread.start()


# method for action of clicking
def click():
    label.config(text=title_list_string)


# Create the main application window
root = tk.Tk()
root.title("Simple PyGUI App")

# Create a label widget
label = tk.Label(root, )
label.pack(pady=5, padx=10)

# Create a button widget
button = tk.Button(root, text="Capture", command=click)
button.pack(pady=5, padx=10)

# Run the Tkinter event loop
root.mainloop()
