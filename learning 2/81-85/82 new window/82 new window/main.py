from tkinter import *


def create_window():
    new_window = Tk()  # Toplevel(): new window on top of other window(s), linked to bottom window.
    # closing bottom window closes top window, but not vice versa. #Tk() creates new independent window
    old_window.destroy()


old_window = Tk()

Button(old_window, text="create new window", command=create_window).pack()
old_window.mainloop()
