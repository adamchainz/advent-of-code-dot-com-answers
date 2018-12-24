#!/usr/bin/env python


def main():
    assert react_polymer(['a', 'A']) == []
    assert react_polymer(['a', 'b', 'B', 'A']) == ['a', 'A']
    assert react_polymer(['a', 'b', 'A', 'B']) == ['a', 'b', 'A', 'B']
    assert react_polymer(['a', 'a', 'b', 'A', 'A', 'B']) == ['a', 'a', 'b', 'A', 'A', 'B']

    with open('5.txt', 'r') as fp:
        polymer = list(fp.read().strip())

    unique_lower_letters = sorted(list(set(x.lower() for x in polymer)))
    stripped_reacted_polymers = [
        fully_react_polymer(strip_polymer(polymer, lower_letter))
        for lower_letter in unique_lower_letters
    ]
    print(min(len(polymer) for polymer in stripped_reacted_polymers))


def strip_polymer(polymer, lower_letter):
    print(lower_letter)
    return [x for x in polymer if x.lower() != lower_letter]


def fully_react_polymer(polymer):
    while True:
        reacted_polymer = react_polymer(polymer)
        if len(reacted_polymer) == len(polymer):
            return reacted_polymer
        polymer = reacted_polymer


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
