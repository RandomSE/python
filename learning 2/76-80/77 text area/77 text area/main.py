from tkinter import *
# text widget: functions like a text area, can have multiple lines of text.


def submit():
    inp = text.get("1.0", END)
    message = Message(window, text=inp)
    message.pack()


window = Tk()
text = Text(window, bg="white", fg="#006400", pady=20, padx=25, font=("Comic sans", 12))
text.pack()
button = Button(window, text="submit", command=submit)
button.pack()
window.mainloop()
