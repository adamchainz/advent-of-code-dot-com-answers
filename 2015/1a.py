#!/usr/bin/env python3
import codecs


def main():
    with codecs.open('1.txt', 'r', 'utf-8') as f:
        instructions = f.read()
    print(instructions.count('(') - instructions.count(')'))

if __name__ == '__main__':
    main()
