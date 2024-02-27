from tkinter import *
# listbox: listing of selectable items from within its own container. similar to radiogroup.


def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have ordered: ", end="\n")

    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    # listbox.delete(listbox.size(), entryBox.get())  # deletes the last one
    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window, bg="#FFFFED", fg="#006400", font=("Comic sans", 23), width=44, height=50,
                  selectmode=MULTIPLE)
listbox.insert(1, "pizza")
listbox.insert(2, "lasagne")
listbox.insert(3, "garlic bread")
listbox.insert(4, "gazpacho")
listbox.insert(5, "pasta")
listbox.config(height=listbox.size())  # useful
listbox.pack()  # can also do .place(co-ordinates)
entryBox = Entry(window,)
entryBox.pack()
addButton = Button(window, text="add", command=add)
addButton.pack()
deleteButton = Button(window, text="delete", command=delete)  # deletes chosen one
deleteButton.pack()
submitButton = Button(window, text="submit", command=submit)
submitButton.pack()
window.mainloop()
