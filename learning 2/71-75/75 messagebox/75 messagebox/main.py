from tkinter import *
from tkinter import messagebox
# message box: self-explanatory

window = Tk()


def click():
    # messagebox.showinfo(title="info", message="You exist")
    # if put in a while(True): loop can be very annoying
    #  messagebox.showwarning(title="warning", message="Death?")
    if messagebox.askyesno(title="cardboard boxes", message="smash?"):
        messagebox.showerror(title="you cannot", message="insufficient boxes")
    # many more messageboxes, but the use cases are fairly similar.
    answer = messagebox.askquestion(title="ask question", message="do you like pie?")
    print(answer)
    check = messagebox.askyesnocancel(title="confused?", message="where?")
    # noinspection PySimplifyBooleanCheck
    if check:
        print("yes")
    elif check == False:  # if not check is not ideal, because then the else statement never executes.
        print("no :c")
    else:
        print(" a ")


button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()
