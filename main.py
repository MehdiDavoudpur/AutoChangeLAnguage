import tkinter as tk
import threading
import time
import pyautogui

# new_app_title is necessary for checking  if app title is changed or not.
new_app_title = ''
# title_list_string is necessary for printing out to user.
last_title = ''
persian_titles = []


def background_task():
    while True:
        global new_app_title
        global last_title
        # get active app title as app_title.
        app_title = pyautogui.getActiveWindowTitle()
        # check if app title is changed or not.
        if app_title != new_app_title:
            # check if app title is changed from  "کافه اینترنشنال" to other thing. new app title here is previous
            # app title really.
            '''i = 0
            for title in title_list:
                if title == app_title:
                    i = 1
            if i == 0:'''
            # app title is not repetitious and is appended to title_list.
            if app_title != 'Auto Change Language':
                if app_title:
                    last_title = app_title
            # check if app title is changed from  per_title to other thing. new app title here is previous
            # app title really.

            for per_title in persian_titles:
                if per_title in new_app_title:
                    # change language from PER to ENG
                    pyautogui.hotkey('shift', 'alt')
                # check if app title is changed from other thing to  per_title
                if app_title:
                    if per_title in app_title:
                        # change language from ENG to PER
                        pyautogui.hotkey('shift', 'alt')

            # refresh app title
            new_app_title = app_title

        time.sleep(0.5)


# Create a thread for the background task
background_thread = threading.Thread(target=background_task)
# Set the thread as a daemon, so it automatically terminates when the main program exits
background_thread.daemon = True
background_thread.start()


# method for action of clicking on get title button.
def get_click():
    text.delete(1.0, 'end')
    text.insert('end', last_title)


# method for action of clicking on set title button.
def set_click():
    persian_titles.append(last_title)


'''def on_text_scroll(*args):
    text1.yview(*args)'''

# Create the main application window
root = tk.Tk()
root.title("Auto Change Language")

# Create a button widget
button = tk.Button(root, text="Get Title", command=get_click)
button.grid(row=0, column=1, pady=5)

# Create a label widget
label = tk.Label(root, text='App Titles:')
label.grid(row=1, column=0, padx=(20, 2), pady=(5, 5))

# Create a text widget
text = tk.Text(root, height=1)
text.grid(row=1, column=1, padx=(2, 20), pady=(5, 5))

'''# Create a Scrollbar widget
scrollbar = tk.Scrollbar(root, command=on_text_scroll)
scrollbar.grid(row=1, column=2, )

# Link Text widget and Scrollbar widget
text1.config(yscrollcommand=scrollbar.set)'''

# Create a button widget
button2 = tk.Button(root, text="Set Title", command=set_click)
button2.grid(row=3, column=1, pady=5)

# Run the Tkinter event loop
root.mainloop()
