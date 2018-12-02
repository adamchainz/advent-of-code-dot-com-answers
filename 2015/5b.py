#!/usr/bin/env python3
import re


def main():
    nice = 0
    with open('5.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if is_nice(line):
                nice += 1
    print(nice)


def is_nice(string):
    return (
        contains_repeated_doublet(string) and
        contains_gapped_repeat(string)
    )


def contains_repeated_doublet(string):
    return re.search(r'(\w{2}).*\1', string)


def contains_gapped_repeat(string):
    return re.search(r'(\w)\w\1', string)


if __name__ == '__main__':
    main()
