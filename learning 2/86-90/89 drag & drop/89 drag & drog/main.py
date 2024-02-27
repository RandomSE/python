from tkinter import *


def drag_in(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y


def drag_out(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


window = Tk()
window.geometry("1080x720")

label = Label(window, text="aAA", bg="#006400", width=8, height=3)
label.place(x=0, y=0)

label2 = Label(window, text="Why", bg="black", width=8, height=3)
label2.place(x=100, y=100)


label.bind("<Button-1>", drag_in)
label.bind("<B1-Motion>", drag_out)  # naming conventions need not apply
label2.bind("<Button-1>", drag_in)
label2.bind("<B1-Motion>", drag_out)
window.mainloop()
