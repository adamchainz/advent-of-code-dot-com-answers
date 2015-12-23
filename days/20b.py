#!/usr/bin/env python3
import itertools
import math
from collections import defaultdict, namedtuple


def main():
    test = list(itertools.islice(house_presents(), 9))
    assert [h.presents for h in test] == [11, 33, 44, 77, 66, 132, 88, 165, 143], test
    matching_houses = (h for h in house_presents() if h.presents >= 34000000)
    print(next(matching_houses).number)


House = namedtuple('House', 'number presents')


def house_presents():
    elves = defaultdict(int)
    for number in itertools.count(start=1):
        house = House(
            number=number,
            presents=sum(11 * n for n in elf_visits(number, elves)),
        )
        yield house


def elf_visits(number, elves):
    large_divisors = []
    for i in range(1, int(math.sqrt(number) + 1)):
        if number % i == 0:
            if elves[i] < 50:
                elves[i] += 1
                yield i
            if i != number // i:
                large_divisors.insert(0, number // i)
    for i in large_divisors:
        if elves[i] < 50:
            elves[i] += 1
            yield i


if __name__ == '__main__':
    main()
