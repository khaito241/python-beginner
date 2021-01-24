'''
Project: Random Password Generator

Password: 
'''

import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def password_generator(length=8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'

    printable = list(printable) #change printable to list so random() is operatable
    random.shuffle(printable)

    random_password = random.choices(printable, k=length)
    random_password = ''.join(random_password)
    return random_password

def get_password_length():
    password_length = input("How long do you want your password: ")
    return int(password_length)

def main():
    password_length = get_password_length()
    password = password_generator(password_length)

    print(password)

if __name__ == '__main__':
    main()