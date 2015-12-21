#!/usr/bin/env python3


def main():
    sues = load_sues()
    suspect = {
        'children': 3,
        'cats': 7,
        'samoyeds': 2,
        'pomeranians': 3,
        'akitas': 0,
        'vizslas': 0,
        'goldfish': 5,
        'trees': 3,
        'cars': 2,
        'perfumes': 1,
    }
    profile = set(suspect.items())
    for sue in sues:
        if all(item in profile for item in sue.items()):
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
