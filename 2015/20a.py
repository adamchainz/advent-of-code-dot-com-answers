#!/usr/bin/env python3
import itertools
import math
from collections import namedtuple


def main():
    test = list(itertools.islice(house_presents(), 9))
    assert [h.presents for h in test] == [10, 30, 40, 70, 60, 120, 80, 150, 130], test
    matching_houses = (h for h in house_presents() if h.presents >= 34000000)
    print(next(matching_houses).number)


House = namedtuple('House', 'number presents')


def house_presents():
    for number in itertools.count(start=1):
        house = House(
            number=number,
            presents=sum(10 * n for n in divisors(number)),
        )
        yield house


def divisors(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i != n // i:
                large_divisors.insert(0, n // i)
    for divisor in large_divisors:
        yield divisor


if __name__ == '__main__':
    main()
