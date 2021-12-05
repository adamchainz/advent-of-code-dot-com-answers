#!/usr/bin/env python
from pathlib import Path

from more_itertools import partition


def search_by_bit(values: list[str], *, most_common: bool) -> str:
    current = values
    for i in range(len(values[0]) + 1):
        if len(current) == 1:
            return current[0]

        def digit_i_is_one(x):
            return x[i] == '1'

        zeroes, ones = partition(digit_i_is_one, current)
        zeroes = list(zeroes)
        ones = list(ones)

        if most_common:
            if len(zeroes) <= len(ones):
                current = ones
            else:
                current = zeroes
        else:
            if len(zeroes) <= len(ones):
                current = zeroes
            else:
                current = ones


if __name__ == '__main__':
    values = Path("3.txt").read_text().splitlines()
    values.sort()

    o2_rating = int(search_by_bit(values, most_common=True), 2)
    co2_rating = int(search_by_bit(values, most_common=False), 2)
    print(o2_rating * co2_rating)
