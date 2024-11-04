import random
import pyperclip
import time

# Create a list of all posible caracters

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

# Get 10 (or length of password) caracters

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

# Create password with chosen caracters

result = car1 + car2 + car3 + car4 + car5 + car6 + car7 + car8 + car9 + car10

# Display password and create file

print("Place name")

name = input()

filename = name + " " + "password" + ".txt"

print("")
print(name)
print(result)
print("Coppied password to clipboard")
file = open(filename, "w")
file.write("Name: ")
file.write(name)
file.write("\n")
file.write("Password: ")
file.write(result)

pyperclip.copy(result)

time.sleep(3)

sys.exit

# done
