import string
from secrets import choice as choice
import os

"""This little password generator creates 10 different passwords and saves them into a textfile on your Desktop. This amount can be changed by editing the 'numbers = x' variable in password_gen."""


def password_opt():
    chars = string.ascii_letters
    chars2 = string.digits
    chars3 = string.punctuation
    chars4 = string.ascii_lowercase
    chars5 = string.ascii_uppercase
    chars6 = chars + chars2 + chars3 + chars4 + chars5

    print(
        "What characters should the password contain? lower & uppercase letters (1), numbers (2), symbols (3) lowercase letters (4), uppercase letters (5), all mixed (6)?\n")

    while True:
        try:
            select = int(input("\n"))
            if select == 1:
                select = chars
            elif select == 2:
                select = chars2
            elif select == 3:
                select = chars3
            elif select == 4:
                select = chars4
            elif select == 5:
                select = chars5
            elif select == 6:
                select = chars6
            return select
        except ValueError:
            print("You haven't entered a number. Please try again\n")


def password_len():
    while True:
        try:
            length = int(input("Length of the Password?\n"))
            return length
        except ValueError:
            print("Please enter a number.\n")


def password_gen(length, select):
    numbers = 10
    fileout = (os.path.expanduser("~") + "\Desktop\pw.txt")
    for x in range(numbers):
        pw = ""
        for c in range(length):
            pw += choice(select)
        print(pw)
        with open(fileout, "a+") as output:
            output.write(pw + "\n")
    print(f'File has been written to {fileout}')


def main():
    options = password_opt()
    length = password_len()
    password_gen(length, options)


if __name__ == "__main__":
    main()
