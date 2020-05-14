from string import ascii_letters as ascii
from string import digits as digits
from string import punctuation as punctuation
from secrets import choice as choice


def password_char():

    """generate a list of all letters (a-z / A-Z, digits (1-10) and special characters"""

    return ascii + digits + punctuation


def generate_pw(charset):

    """ Using list comprehension to generate a 40-characters password with the information of password_char()"""

    return ''.join((choice(charset) for _ in range(40)))


def main():
    stub = password_char()
    password = generate_pw(stub)
    print(password)


if __name__ == "__main__":
    main()
