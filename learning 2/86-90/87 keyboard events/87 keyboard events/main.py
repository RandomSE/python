from tkinter import *
from tkinter import messagebox


def key(event):
    messagebox.showinfo("You pressed: ", message=event.keysym)
    label.config(text=event.keysym)
    if event.keysym == "f":
        messagebox.showinfo("You honour the fallen.", message="Respect has been paid")


window = Tk()
window.bind("<Key>", key)  # must be capitalised for all keys
label = Label(window, text="hmm?", font=("Comic sans", 24))
label.pack()
window.mainloop()
