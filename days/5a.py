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
        num_vowels(string) >= 3 and
        contains_double(string) and
        not contains_banned_doublet(string)
    )


def num_vowels(string):
    return sum(
        1 for c in string
        if c in 'aeiou'
    )


def contains_double(line):
    return re.search(r'(\w)\1', line) is not None


def contains_banned_doublet(string):
    return (
        'ab' in string or
        'cd' in string or
        'pq' in string or
        'xy' in string
    )


if __name__ == '__main__':
    main()
