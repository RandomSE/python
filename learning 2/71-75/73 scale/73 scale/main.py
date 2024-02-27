from tkinter import *
# scale: sliding scale.

# hot_pic = PhotoImage(file="hot.png") # hotlabel = Label(image=hot_pic) # hotlabel.pack()
# cold_pic = PhotoImage(file="cold.png") # coldlabel = Label(image=cold_pic) # coldlabel.pack()


def submit():
    temperature = scale.get()
    print("The temperature is " + str(temperature) + " degrees celsius")
    # instead of adding images, will just add a print
    if temperature >= 20:
        print("warm.")
    else:
        print("decent.")


window = Tk()
scale = Scale(window, from_=0, to=40, length=450, width=50, orient=VERTICAL,
              font=("Comic sans", 23), tickinterval=5,  # adds numeric intervals
              showvalue=False,  # will hide the curr value
              resolution=1, troughcolor="black", fg="#006400", bg="white",
              )
scale.set((scale["to"]-scale["from"])/2)  # could add + scale["from"] if from > 0, would do max-min value
scale.pack()
button = Button(window, text="submit temperature", command=submit)
button.pack()

window.mainloop()
