#!/usr/bin/env python3

def main():
    string = '1113222113'
    for i in range(50):
        string = expand(string)
    print(len(string))


def expand(string):
    current = string[0]
    count = 1
    expanded = ''
    for char in string[1:]:
        if char == current:
            count += 1
        else:
            expanded += str(count) + current
            count = 1
            current = char
    expanded += str(count) + current
    return expanded


if __name__ == '__main__':
    main()
