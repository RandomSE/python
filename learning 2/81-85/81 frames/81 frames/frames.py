from tkinter import *


window = Tk()
frame = Frame(window, bg="salmon", width=70, height=100, relief=RAISED)
frame.place(x=0, y=0)
Button(frame, text="W", font=("Comic sans", 23), width=3).pack(side=TOP)
Button(frame, text="A", font=("Comic sans", 23), width=3).pack(side=LEFT)
Button(frame, text="S", font=("Comic sans", 23), width=3).pack(side=RIGHT)
Button(frame, text="D", font=("Comic sans", 23), width=3).pack(side=BOTTOM)
# unnamed, do not need to be assigned to vars.

window.mainloop()
