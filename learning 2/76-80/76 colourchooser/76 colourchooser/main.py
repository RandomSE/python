from tkinter import *
from tkinter import colorchooser
# submodule, not included in import *, also color=colour, but... semantics.

window = Tk()


def click():
    window.config(bg=colorchooser.askcolor()[1])  # vital for customization


button = Button(text="click me", command=click)
button.pack()
window.geometry("1080x720")
window.mainloop()
