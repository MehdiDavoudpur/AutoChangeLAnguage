import tkinter as tk  # for creating UI
import threading  # for monitoring active app in background task
import time  # for handling sleep time
import pyautogui  # for getting active app title of windows
import database  # for saving app titles

app_title = ''  # for saving title of activating app
last_title = ''  # for saving the title that is not: 1.'Auto Change Language' 2. previous_title
previous_title = ''  # for comparing with last_title
persian_titles = []  # for save selected app_titles in database


def background_task():  # for monitoring active app

    while True:  # a continuous loop
        global app_title, last_title, previous_title
        previous_language = 'ENG'  # by default languages are 'ENG'
        last_language = 'ENG'  # by default languages are 'ENG'

        app_title = str(pyautogui.getActiveWindowTitle())  # get active app title as last_title.
        if app_title:  # for avoiding last_title is Non Type.
            if app_title != previous_title:  # checking if app title is changed or not.
                if app_title != 'Auto Change Language':  # by clicking on this app for getting last_title,
                    # last_title is 'Auto Change Language' always. It's necessary to exclude this title.
                    last_title = app_title

                    print(f'\nprevious_title = {previous_title} \nlast_title = {last_title}\n')
                    for persian_title in persian_titles:  # survey and compare previous_title and app_title with all
                        # persian_titles.

                        print(f'persian_title = {persian_title}')

                        if persian_title == previous_title:
                            previous_language = 'PER'

                        if persian_title == last_title:
                            last_language = 'PER'

                    print(f'\nprevious_lang is {previous_language} & last_lang is {last_language}\n')
                    if previous_language == 'ENG' and last_language == 'PER':
                        pyautogui.hotkey('shift', 'alt')  # change language from ENG to PER.
                    if previous_language == 'PER' and last_language == 'ENG':
                        pyautogui.hotkey('shift', 'alt')  # change language from PER to ENG.

                previous_title = last_title  # refresh app title

        time.sleep(0.5)  # slow the monitoring to avoid excessive ram usage


# Create a thread for the background task
background_thread = threading.Thread(target=background_task)
# Set the thread as a daemon, so it automatically terminates when the main program exits
background_thread.daemon = True
background_thread.start()


# method for action of clicking on get title button
def get_click():
    txt1.delete(1.0, 'end')
    txt1.insert('end', last_title)


# method for action of clicking on set title button
def set_click():
    # persian_titles.append(last_title)
    database.insert(last_title)


def show_click():
    global persian_titles
    persian_titles = database.show()
    # print(persian_titles)
    txt2.delete(1.0, 'end')
    for persian_title in persian_titles:
        txt2.insert('end', persian_title + '\n')


# def delete_click():


# Create the main application window
root = tk.Tk()
root.title("Auto Change Language")

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


def widget_block_1(parent):
    # Create a frame to hold the widgets
    frame = tk.Frame(parent, borderwidth=2, relief="ridge")

    # Add some widgets to the frame
    # Create button widgets
    btn1 = tk.Button(frame, text="Get", command=get_click)
    btn2 = tk.Button(frame, text="Set", command=set_click)
    btn3 = tk.Button(frame, text="Show", command=show_click)
    btn4 = tk.Button(frame, text="Delete", command=get_click)

    # Use pack() to organize the widgets in the frame
    btn1.grid(row=0, column=0, padx=2)
    btn2.grid(row=0, column=1, padx=2)
    btn3.grid(row=0, column=2, padx=2)
    btn4.grid(row=0, column=3, padx=2)

    return frame


# Create multiple blocks of widgets
block1 = widget_block_1(root)

# Use grid() to organize the blocks in rows and columns
block1.grid(row=0, column=1, padx=10, pady=10)


def widget_block_2(parent):
    # Create a frame to hold the widgets
    frame = tk.Frame(parent, borderwidth=2, relief="ridge")

    # Add some widgets to the frame
    # Create button widgets
    btn1 = tk.Button(frame, text="Delete All", command=get_click)
    btn2 = tk.Button(frame, text="Exit", command=get_click)

    # Use pack() to organize the widgets in the frame
    btn1.grid(row=0, column=0, padx=(2, 30))
    btn2.grid(row=0, column=1, padx=(30, 2))

    return frame


# row 1
lbl1 = tk.Label(root, text='Active App Title:')
lbl1.grid(row=1, column=0, padx=(20, 2), pady=(5, 5), sticky='e')

txt1 = tk.Text(root, height=1, width=50)
txt1.grid(row=1, column=1, padx=(2, 2), pady=(5, 5))

# row 2
lbl2 = tk.Label(root, text='All Set Titles:')
lbl2.grid(row=2, column=0, padx=(20, 2), pady=(5, 5), sticky='e')


def on_text_scroll(*args):
    txt2.yview(*args)


txt2 = tk.Text(root, height=25, width=50)
txt2.grid(row=2, column=1, padx=(2, 2), pady=(5, 5), sticky="ns")

# Create a Scrollbar widget
scrollbar = tk.Scrollbar(root, command=on_text_scroll)
scrollbar.grid(row=2, column=2, sticky="ns")

# row 3
block2 = widget_block_2(root)
block2.grid(row=3, column=1, padx=10, pady=10)

show_click()

root.mainloop()
