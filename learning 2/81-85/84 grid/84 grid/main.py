from tkinter import *
# grid() geometry manager, organizes widgets in a table-like structure.


def submit():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    email_address = email_address_entry.get()
    if (len(first_name) > 0) and (len(last_name) > 0) and (len(email_address) > 0):
        print("Welcome, " + first_name + " " + last_name + " and your email address is " + email_address)
    else:
        print("You did not enter any details.")


window = Tk()

# declaring grids separately because the yellow lines are annoying, the functions would return None.
titleLabel = Label(window, text="enter your info", font=("Comic sans", 27), bg="#006400")
titleLabel.grid(row=0, column=0, columnspan=2)

first_name_label = Label(window, text="First name", width=23, bg="red")
first_name_label.grid(row=1, column=0)
first_name_entry = Entry(window)
first_name_entry.grid(row=1, column=1)

last_name_label = Label(window, text="Last name", width=23, bg="yellow")
last_name_label.grid(row=2, column=0)
last_name_entry = Entry(window)
last_name_entry.grid(row=2, column=1)

email_address_label = Label(window, text="Email address", width=23, bg="blue")
email_address_label.grid(row=3, column=0)
email_address_entry = Entry(window)
email_address_entry.grid(row=3, column=1)

submit_button = Button(text="Submit", command=submit)
submit_button.grid(row=4, column=0, columnspan=2)
window.mainloop()
