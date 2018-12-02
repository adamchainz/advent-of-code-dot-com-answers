#!/usr/bin/env python3
import codecs


def main():
    with codecs.open('1.txt', 'r', 'utf-8') as f:
        instructions = f.read()

    f = 0
    for i, char in enumerate(instructions, 1):
        if char == '(':
            f += 1
        else:
            f -= 1
        if f < 0:
            print(i)
            break

if __name__ == '__main__':
    main()
