#!/usr/bin/env python3
import re

def main():
    password = "cqjxxyzz"
    i = 0
    while True:
        password = increment_string(password)
        if is_valid(password):
            print(password)
            break


def increment_string(string):
    if string == '':
        # Fully wrapped
        return 'a'
    elif string[-1] == 'z':
        return increment_string(string[:-1]) + 'a'
    # Skip i, o, l in increments
    elif string[-1] == 'g':
        return string[:-1] + 'j'
    elif string[-1] == 'k':
        return string[:-1] + 'm'
    else:
        return string[:-1] + chr(ord(string[-1]) + 1)


def is_valid(password):
    return (
        'i' not in password and
        'o' not in password and
        'l' not in password and
        contains_two_pairs(password) and
        contains_straight(password)
    )


def contains_straight(string):
    straight = 1
    ord_last = ord(string[0])
    for char in string[1:]:
        if ord(char) == ord_last + 1:
            straight += 1
            if straight == 3:
                return True
        else:
            straight = 1
        ord_last = ord(char)
    return False


two_pairs_re = re.compile(r'(\w)\1.+(\w(?<!\1))\2')

def contains_two_pairs(string):
    return two_pairs_re.search(string)


if __name__ == '__main__':
    main()
