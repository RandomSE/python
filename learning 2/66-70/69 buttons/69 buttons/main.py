
# button: clickable, more easily utilized widgets
from tkinter import *


count = 0


window = Tk()
window.geometry("1080x720")


def click():
    global count
    count += 1
    if count <= 20:
        print(count)
    elif 30 > count > 20:
        print("Cease petting the cat.")
        print(count)
    else:
        print("Run.")
        # does not have any functionality aside from this. in later projects might use update function


def check(number):
    global count
    if number < 30:
        pass
    else:
        print("Mistakes were made.")


photo2 = PhotoImage(file="angrycat.png")
photo = PhotoImage(file="buttercat.png")
button = Button(window, text="pat the cat", command=click, font=("Comic Sans", 43), fg="cyan", bg="black",
                activebackground="black", activeforeground="cyan", state=ACTIVE, image=photo, compound="top")


button.pack()
window.mainloop()
