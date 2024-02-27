# like checkbox, but can only choose one.
from tkinter import *


def order():
    if x.get() == 0:
        print("you choose lasagne. correct choice.")
    elif x.get() == 1:
        print("You choose pizza.")
    elif x.get() == 2:
        print("You choose salad. Healthy.")
    else:
        print("You did not order.")


food = ["lasagne", "pizza", "salad"]
window = Tk()
# photo, not needed here though. use image= name, + compound =
x = IntVar()
for i in range(len(food)):
    radio = Radiobutton(window, text=food[i], font=("Comic sans", 20), value=i,  variable=x,
                        padx=10, pady=13, indicatoron=0, width=200, command=order)
    radio.pack(anchor=W)
window.mainloop()
