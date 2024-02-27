# checkboxes: objects with boolean value
from tkinter import *


def display():
    if x.get():
        print("You agree.")
    else:
        print("You do not agree.")


window = Tk()
x = BooleanVar()
butter_cat = PhotoImage(file="buttercat.png")

check_button = Checkbutton(window, text="I agree that this cat is edited(not buttered)",
                           variable=x, onvalue=True, offvalue=False, command=display, font=("Comic sans", 23, "bold"),
                           bg="gray", fg="blue", activebackground="gray", activeforeground="blue", padx=20, pady=10,
                           image=butter_cat, compound=LEFT)
check_button.pack()


window.mainloop()
