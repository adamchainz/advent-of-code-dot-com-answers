#!/usr/bin/env python
from collections import Counter


def main():
    with open('2.txt', 'r') as fp:
        box_ids = [x.strip() for x in fp.readlines()]

    num_exactly_two = 0
    num_exactly_three = 0
    for box_id in box_ids:
        counts = Counter(box_id).values()
        if 2 in counts:
            num_exactly_two += 1
        if 3 in counts:
            num_exactly_three += 1
    print(num_exactly_two * num_exactly_three)


if __name__ == '__main__':
    main()
