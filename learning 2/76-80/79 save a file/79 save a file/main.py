from tkinter import *
from tkinter import filedialog
import os


def savefile():
    current_dir = os.getcwd()  # finds the relative directory; makes it more universal.
    try:
        file = filedialog.asksaveasfile(defaultextension=".txt",
                                        filetypes=[("Text file", ".txt"), ("Html", ".html")],
                                        initialdir=current_dir)
        # instead of try... except could also do if file is None: return
        # content = str(text.get("1.0", END))
        content = input("Enter what you want to be saved: ")
        file.write(content)
        file.close()
    except AttributeError:
        print("You did not save a file.")  # try... except to prevent program not running.


window = Tk()
button = Button(window, text="save", command=savefile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
