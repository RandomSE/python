from tkinter import *
from tkinter import filedialog


window = Tk()


open_icon = PhotoImage(file="open.png")
exit_icon = PhotoImage(file="exit.png")
save_icon = PhotoImage(file="save.png")


def openfile():
    filedialog.askopenfilename()


def savefile():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:  # to prevent error stopping program
        print(f"File saved at: {file_path}")
    else:
        print("No file saved.")


def cut():
    print(None)


def copy_code():
    print("copy was taken.")


def paste():
    print(None)


menubar = Menu(window)
window.config(menu=menubar)
fileMenu = Menu(menubar, tearoff=0, font=("Comic sans", 23, "bold"))

menubar.add_cascade(label="File", menu=fileMenu)  # IMPORTANT: put the correct menu or will not work.
fileMenu.add_command(label="Open", command=openfile,  image=open_icon, compound=LEFT)
fileMenu.add_command(label="Save", command=savefile, image=save_icon, compound=LEFT)
fileMenu.add_separator()  # adds a seperator
fileMenu.add_command(label="Exit", command=quit, image=exit_icon, compound=LEFT)

editMenu = Menu(window, tearoff=0, font=("Comic sans", 23, "bold"))
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy_code)
editMenu.add_command(label="Paste", command=paste)


window.mainloop()
