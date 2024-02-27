from tkinter import *
import time
# for constant, naming conv is all uppercase.

HEIGHT = 540  # for the space image
WIDTH = 700  # for the space image
xVelocity = 5
yVelocity = 2


window = Tk()
umbrella = PhotoImage(file="mini_umbrella.png")
spaceImage = PhotoImage(file="pngwing.com.png")
canvas = Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()
bg_image = canvas.create_image(0, 0, image=spaceImage)
my_image = canvas.create_image(0, 0, image=umbrella, anchor=NW)


image_width = umbrella.width()
image_height = umbrella.height()

while True:
    coordinates = canvas.coords(my_image)
    print(coordinates)
    if (coordinates[0] >= WIDTH - image_width) or (coordinates[0] < 0):
        xVelocity = xVelocity * -1
    if (coordinates[1] >= HEIGHT - image_height) or (coordinates[1] < 0):
        yVelocity = yVelocity * -1
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()
    time.sleep(0.01)


window.mainloop()
