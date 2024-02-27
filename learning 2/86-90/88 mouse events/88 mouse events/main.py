from tkinter import *
from tkinter import messagebox


window = Tk()


def check(event):
    messagebox.showinfo("e", message="mouse coordinates: " + str(event.x) + "," + str(event.y))


window.bind("<Button-1>", check)  # 1= leftClick, 2= scrollWheel, 3=rightClick
# ButtonRelease triggers event when letting go of held mouse button.
# Enter : where you enter window. Leave: where you leave window. Motion: triggers while in motion
window.geometry("1080x720")
window.mainloop()
