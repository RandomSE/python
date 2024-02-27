from tkinter import *
from tkinter import ttk


window = Tk()
notebook = ttk.Notebook(window)  # widget. manages collection of windows & displays.
tab_1 = Frame(notebook)  # new frame for notebook.
tab_2 = Frame(notebook)

notebook.add(tab_1, text="page 1")
notebook.add(tab_2, text="page 2")
notebook.pack(expand=True, fill=BOTH)  # expands to fill any space that is unoccupied. Fill fills space on x/y-axis.

Label(tab_1, text="Hello, welcome to tab 1", width=40, height=35, font=("Comic sans,", 35)).pack()
Label(tab_2, text="Hello, welcome to tab 2", width=40, height=35, font=("Comic sans,", 35)).pack()


window.mainloop()
