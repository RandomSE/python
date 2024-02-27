# Graphic User Interface
# windows: serves as container, holds widgets.
# widgets: GUI elements such as buttons, textboxes, labels, etc.
# put into command window: pip install Pillow
import tkinter
from tkinter import *
import os

window_1 = Tk()  # instantiate an instance of a window
window_1.geometry("900x486")  # could add customization options. this size is for the cat
window_1.title("The one")


script_directory = os.path.dirname(os.path.abspath(__file__))
butter_cat_path = os.path.join(script_directory, "buttercat.png")

try:
    butter_cat = tkinter.PhotoImage(file=butter_cat_path)
    window_1.iconphoto(True, butter_cat)  # more butter cat
    label = tkinter.Label(window_1, image=butter_cat)
    label.pack()
except tkinter.TclError as e:
    print(f"Error loading image: {e}")

window_1.config(background="#000000")  # does not have a background yet

window_1.mainloop()  # place window on computer screen, listen for events
print("Behold the glory of the butter cat")
