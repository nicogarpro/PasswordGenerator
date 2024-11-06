import random
import pyperclip
from tkinter import *

list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "-",
    "_",
    "=",
    "+",
]

car1 = random.choice(list)

car2 = random.choice(list)

car3 = random.choice(list)

car4 = random.choice(list)

car5 = random.choice(list)

car6 = random.choice(list)

car7 = random.choice(list)

car8 = random.choice(list)

car9 = random.choice(list)

car10 = random.choice(list)

result = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10

root = Tk()
root.geometry("400x300")


label = Label(root, text="Enter the name of your platform")
label.grid(row=0, column=0)

entry = Entry(root)
entry.grid(row=1, column=0)

def text():
    textname = entry.get()
    filename = textname + " " + "password" + ".txt"
    file = open(filename, "x")
    file.write("Name: ")
    file.write(textname)
    file.write("\n")
    file.write("Password: ")
    file.write(result)
    pyperclip.copy(result)
    #----------------------
    label2 = Label(root, text=" Password saved in: " + filename + " \nand coppied to clipboard.")
    label2.grid(row=4, column=0)
    #----------------------
    button2 = Button(root, text="Quit", command=quit)
    button2.grid(row=3, column=0)

button = Button(root, text="Go", command=text)
button.grid(row=1, column=1)

root.mainloop()
