#!/usr/bin/env python


def main():
    assert react_polymer(['a', 'A']) == []
    assert react_polymer(['a', 'b', 'B', 'A']) == ['a', 'A']
    assert react_polymer(['a', 'b', 'A', 'B']) == ['a', 'b', 'A', 'B']
    assert react_polymer(['a', 'a', 'b', 'A', 'A', 'B']) == ['a', 'a', 'b', 'A', 'A', 'B']

    with open('5.txt', 'r') as fp:
        polymer = list(fp.read().strip())

    while True:
        reacted_polymer = react_polymer(polymer)
        if reacted_polymer == polymer:
            break
        polymer = reacted_polymer

    print(len(reacted_polymer))


def react_polymer(polymer):
    new_polymer = []
    skip = False
    for c, d in zip(polymer, polymer[1:] + ['']):
        if skip:
            skip = False
            continue
        if c != d and (c == d.lower() or c.lower() == d):
            skip = True
            continue
        new_polymer.append(c)

    return new_polymer


if __name__ == '__main__':
    main()
