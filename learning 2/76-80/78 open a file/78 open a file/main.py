from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = (filedialog.askopenfilename
                (initialdir="C:\\Users\\the11\\PycharmProjects\\learning\\76-80\\78 open a file\\78 open a file",
                 title="open a file", filetypes=[("text files", "*.txt"), ("all files", "*.*")]))
    with open(filepath, "r") as file:
        print(file.read())  # do not need closeFile here, as with is used.
        # could also set the contents to a string variable, which could be manipulated.


window = Tk()
button = Button(window, text="open", command=openfile)
button.pack()
window.mainloop()
