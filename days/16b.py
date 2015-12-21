#!/usr/bin/env python3
from operator import eq, gt, lt


def main():
    sues = load_sues()
    suspect = {
        'children': (eq, 3),
        'cats': (gt, 7),
        'samoyeds': (eq ,2),
        'pomeranians': (lt, 3),
        'akitas': (eq, 0),
        'vizslas': (eq, 0),
        'goldfish': (lt, 5),
        'trees': (gt, 3),
        'cars': (eq, 2),
        'perfumes': (eq, 1),
    }

    for sue in sues:
        matched = True
        for attr, val in sue.items():
            op, target = suspect.get(attr)
            if not op(val, target):
                matched = False
        if matched:
            print(sue.number)


class Sue(dict):
    def __init__(self, number):
        self.number = number


def load_sues():
    sues = []
    with open('16.txt', 'r', encoding='utf-8') as f:
        for line in f:
            number, facts = line[len('Sue '):].split(':', 1)
            sue = Sue(int(number))
            for part in facts.strip().split(','):
                fact, count = part.split(':')
                sue[fact.strip()] = int(count.strip())
            sues.append(sue)
    return sues


if __name__ == '__main__':
    main()
