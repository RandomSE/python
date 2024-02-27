# entry widget: accepts one line of input from user.
from tkinter import *

window = Tk()


def submit():
    username = entry.get()
    print(username)
    entry.config(state=DISABLED)
    return username


def delete():
    entry.delete(0, END)


def backspace():
    length = len(entry.get())
    entry.delete(length-1, END)


window.geometry("1080x720")
entry = Entry(window, font=("Comic sans", 50), fg="#000000", bg="turquoise", show="&")
entry.insert(0, "username")
entry.pack(side=LEFT)
submit_button = Button(window, text="submit text", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete text", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="remove 1 char", command=backspace)
backspace_button.pack(side=RIGHT)
window.mainloop()
