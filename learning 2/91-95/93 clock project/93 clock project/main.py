from time import *
from tkinter import *
from tkinter import messagebox


def update():
    time_string = strftime("%I:%M:%S %p")
    labelTime.config(text=time_string)

    labelTime.after(1000, update)  # ah... good old recursive functions. do not put parentheses.

    day_string = strftime("%Y %B %d %A")
    labelDay.config(text=day_string)

    # window.after(1000, update)  # not used as the day does not change enough for this.
    # I have added a button for this, however.


def check():
    day_string = strftime("%Y %B %d %A")
    labelDay.config(text=day_string)
    messagebox.showinfo(title="updated date: ", message=day_string)


window = Tk()
labelTime = Label(window, text="current time: ", font=("Comic sans", 23), fg="#006400", bg="white")
labelTime.pack()

labelDay = Label(window, text="current date: ", font=("Arial", 30, "bold"), fg="black", bg="white")
labelDay.pack()

buttonDay = Button(window, text="Check the current date: ", command=check)
buttonDay.pack()

update()
window.mainloop()
