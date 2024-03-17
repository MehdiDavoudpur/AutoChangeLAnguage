import tkinter as tk
import threading
import time
import pyautogui
import database

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
            # check if app title is changed from  per_title to other thing. new app title here is previous
            # app title really.
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
    txt1.delete(1.0, 'end')
    txt1.insert('end', last_title)


# method for action of clicking on set title button.
def set_click():
    persian_titles.append(last_title)
    database.insert(last_title)


def show_click():
    all_set_titles = database.show()
    print(all_set_titles)
    txt2.delete(1.0, 'end')
    txt2.insert('end', all_set_titles)


# Create the main application window
root = tk.Tk()
root.title("Auto Change Language")


def resize(event):
    # Adjust the widget size when the window is resized
    canvas.config(width=event.width, height=event.height)


root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)


def widget_block_1(parent):
    # Create a frame to hold the widgets
    frame = tk.Frame(parent, borderwidth=2, relief="ridge")

    # Add some widgets to the frame
    # Create button widgets
    btn1 = tk.Button(frame, text="Get", command=get_click)
    btn2 = tk.Button(frame, text="Set", command=get_click)
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

canvas = tk.Canvas(root, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

canvas.bind("<Configure>", resize)

root.mainloop()
