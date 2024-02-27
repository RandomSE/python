from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import time


def start():
    GB = 75
    download = 0
    speed = 0.25  # speedy
    while download < GB:
        time.sleep(0.04)
        download += speed
        bar["value"] += (speed/GB) * 100
        percent.set(str(int((download / GB) * 100)) + "%")
        text.set(str(round(download, 2)) + "/" + str(GB) + " GB downloaded.")
        window.update_idletasks()  # shows the progress
        if bar["value"] == 100:
            messagebox.showinfo(title="Download progress:.", message="Download completed.")


window = Tk()

percent = StringVar()
text = StringVar()

bar = Progressbar(window, orient=HORIZONTAL, length=400)
bar.pack(pady=10)

percentLabel = Label(window, textvariable=percent)
percentLabel.pack()

taskLabel = Label(window, textvariable=text)
taskLabel.pack()

equalsButton = Button(window, text="download", command=start)
equalsButton.pack()


window.mainloop()
