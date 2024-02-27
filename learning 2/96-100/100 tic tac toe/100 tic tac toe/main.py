from tkinter import *
import random  # change to make it ultimate tic-tac-toe ( 9 blocks of 3 x 3 )


# to stop the yellow errors that don't hinder program:
# noinspection PyTypeChecker
def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player  # checks the text of the button

            if check_winner() is False:
                player = players[1]
                label.config(text=players[1] + " turn")
            elif check_winner() is True:
                label.config(text=players[0] + " wins")
            elif check_winner() == "Tie":
                label.config(text="Tie")
        else:
            buttons[row][column]["text"] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=players[0] + " turn")
            elif check_winner() is True:
                label.config(text=players[1] + " wins")
            elif check_winner() == "Tie":
                label.config(text="Tie")


def check_winner():
    for row in range(3):
        if buttons[row][0]["text"] == buttons[row][1]["text"] == buttons[row][2]["text"] != "":
            buttons[row][0].config(bg="#006400")
            buttons[row][1].config(bg="#006400")
            buttons[row][2].config(bg="#006400")
            return True

    for column in range(3):
        if buttons[0][column]["text"] == buttons[1][column]["text"] == buttons[2][column]["text"] != "":
            buttons[0][column].config(bg="red")
            buttons[1][column].config(bg="red")
            buttons[2][column].config(bg="red")
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        buttons[0][0].config(bg="orange")
        buttons[1][1].config(bg="orange")
        buttons[2][2].config(bg="orange")
        return True

    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        buttons[0][2].config(bg="yellow")
        buttons[1][1].config(bg="yellow")
        buttons[2][0].config(bg="yellow")
        return True

    elif empty_space() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="purple")
        return "Tie"

    else:
        return False


def empty_space():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="white")


window = Tk()
window.title("Tic Tac Toe")
players = ["x", "o"]  # can be changed
player = random.choice(players)
buttons = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
label = Label(text=player + " turn", font=("Consolas", 23))
label.pack(side="top")
reset_button = Button(text="Reset", font=("Arial", 22), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        # noinspection PyTypeChecker
        buttons[row][column] = Button(frame, text="", font=("Comic sans", 23), width=7,
                                      height=3, command=lambda row1=row, column1=column: next_turn(row1, column1))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
