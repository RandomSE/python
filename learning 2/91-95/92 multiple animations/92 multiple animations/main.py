from tkinter import *
from time import *
from balls import *
# could also add option to add/remove the spheres

WIDTH = 1080
HEIGHT = 720
window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
ball1 = Ball(canvas, 70, 30, 200, -2, 1, "green")
ball2 = Ball(canvas, 30, 70, 50, 14, -8, "blue")
ball3 = Ball(canvas, 323, 200, 100, -7, 0.5, "black")
ball4 = Ball(canvas, 500, 300, 175, 1, -7, "red")


while True:
    ball1.move()
    ball2.move()
    ball3.move()
    ball4.move()
    window.update()
    sleep(0.05)

window.mainloop()

