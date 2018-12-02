#!/usr/bin/env python3
import operator
import itertools
from functools import reduce


def main():
    test = best_first_entanglement(example_packages, 4)
    assert test == 44, test

    print(best_first_entanglement(packages, 4))


example_packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

packages = [
    1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 67, 71, 73,
    79, 83, 89, 97, 101, 103, 107, 109, 113,
]


def pick(total, items, head_size=None):
    # yield all ways of partitioning 'items' into two sets: the first summing
    # 'total', and the rest

    if head_size == 0:
        return

    for i, item in enumerate(items):
        if item <= total:
            if item == total and (head_size is None or head_size == 1):
                yield [item], items[:i] + items[i + 1:]
            else:
                sub_total = total - item
                sub_head_size = None if head_size is None else head_size - 1
                for sub_list, others in pick(sub_total, items[i + 1:], sub_head_size):
                    yield [item] + sub_list, items[:i] + others


def entanglement(items):
    return reduce(operator.mul, items, 1)


def best_first_entanglement(packages, compartments):
    total_weight = sum(packages)
    assert total_weight % compartments == 0
    one_third_weight = total_weight // compartments

    for num_front_group in range(1, len(packages) + 1):
        best = None
        for split, others in pick(one_third_weight, packages, num_front_group):
            if best is None:
                best = split
            elif entanglement(split) < entanglement(best):
                best = split

        if best is not None:
            return entanglement(best)

if __name__ == '__main__':
    main()
