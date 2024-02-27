# labels: area widget that holds text and/or an image in a window
from tkinter import *

window = Tk()
photo = PhotoImage(file="label1.png")
window.geometry("1920x1080")
label = Label(window, text="Hello. ", font=("Comic Sans", 50, "bold"), fg="green", bg="#000000",
              relief=RAISED, bd=120, padx=100, pady=100, image=photo, compound="top")
label.place(x=540, y=360)
label.pack()

window.mainloop()
