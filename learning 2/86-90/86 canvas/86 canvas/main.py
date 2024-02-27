from tkinter import *
# canvas: widget used to draw stuff in a window.


window = Tk()
canvas = Canvas(window, height=420, width=700)
# greenLine = canvas.create_line(0, 0, 700, 420, fill="#006400", width=10)  # width then height.
# purpleLine = canvas.create_line(0, 420, 700, 0, fill="magenta", width=10)  # most recently created one appears on top.
# canvas.create_rectangle(10, 10, 700, 420, width=25, fill="maroon")
# canvas.create_polygon(350, 0, 0, 420, 700, 420, fill="green", outline="brown", width=20)  # chunky triangle
# canvas.create_arc(0, 0, 700, 420, fill="orange", style=PIESLICE, extent=360)
canvas.create_arc(0, 0, 700, 420, fill="red", extent=180, width=3, outline="black")
canvas.create_arc(0, 0, 700, 420, fill="white", extent=180, width=3, start=180, outline="black")
canvas.create_oval(280, 168, 420, 252, width=20, fill="white")
canvas.pack()
window.mainloop()
