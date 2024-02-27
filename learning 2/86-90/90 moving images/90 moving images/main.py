from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)


def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)


def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())


window = Tk()
window.geometry("1080x720")

window.bind("<w>", move_up)
window.bind("<a>", move_left)
window.bind("<s>", move_down)
window.bind("<d>", move_right)

ButterCat = PhotoImage(file="buttercat.png")  # buttercat speaks to me on a primal level
secretLabel = Label(window, text="The cat is gone :c")
secretLabel.place(x=540, y=0)
label = Label(window, image=ButterCat)
label.pack()
window.mainloop()
