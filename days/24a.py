#!/usr/bin/env python3
import operator
import itertools
from functools import reduce


def main():
    test = naive_best_grouping(example_packages)
    assert set(test[0]) == {9, 11}, test
    # takes forever
    # best = naive_best_grouping(packages)
    # print(best[0].qe)
    # test = list(pick(2, [2, 2]))
    # assert test == [([2], [2]), ([2], [2])], test
    test = list(pick(3, [1, 4]))
    assert test == [], test
    test = list(pick(4, [1, 3, 4]))
    assert test == [([1, 3], [4]), ([4], [1, 3])], test
    # test = list(equal_pick(3, [2, 2]))
    # assert test == [], test
    # test = list(equal_pick(2, [2, 2]))
    # assert test == [[[2], [2]], [[2], [2]]], test

    test = best_first_entanglement(example_packages)
    assert test == 99, test

    print(best_first_entanglement(packages))


example_packages = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]

packages = [
    1, 3, 5, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 67, 71, 73,
    79, 83, 89, 97, 101, 103, 107, 109, 113,
]


# naive algo


class NaiveGroup(list):
    @property
    def weight(self):
        return sum(self)

    @property
    def qe(self):
        return reduce(operator.mul, self, 1)


def naive_groupings(n, r):
    rs = list(range(1, r + 1))
    yield from itertools.product(*[rs for x in range(n)])


def naive_package_groupings(packages, num_groups=3):
    for grouping in naive_groupings(len(packages), 3):  # 3 groups always
        groups = [NaiveGroup() for x in range(num_groups)]
        for package, group_num in zip(packages, grouping):
            groups[group_num - 1].append(package)
        yield groups


def naive_best_grouping(packages):
    best = None
    for grouping in naive_package_groupings(packages):
        if (
            grouping[0].weight != grouping[1].weight or
            grouping[1].weight != grouping[2].weight
        ):
            continue
        if best is None:
            best = grouping
        else:
            if len(grouping[0]) < len(best[0]):
                best = grouping
            elif (
                len(grouping[0]) == len(best[0]) and
                grouping[0].qe < best[0].qe
            ):
                best = grouping
    return best


# smart


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


def equal_pick(num_ways, items):
    if num_ways == 1:
        yield [items]
    else:
        total = sum(items)
        if total % num_ways == 0:
            for group, others in pick(total // num_ways, items):
                for sub_splits in equal_pick(num_ways - 1, others):
                    split = [group] + sub_splits
                    yield split


def still_naive_best_grouping(packages):
    packages = sorted(packages, reverse=True)
    best = None
    for i, grouping in enumerate(equal_pick(3, packages)):
        if i % 1000 == 0:
            print(i)
            print(best)
            if best is not None:
                print(entanglement(best[0]))
        if best is None:
            best = grouping
        else:
            if len(grouping[0]) < len(best[0]):
                best = grouping
            elif (
                len(grouping[0]) == len(best[0]) and
                entanglement(grouping[0]) < entanglement(best[0])
            ):
                best = grouping
    return best


def entanglement(items):
    return reduce(operator.mul, items, 1)


def best_first_entanglement(packages):
    total_weight = sum(packages)
    assert total_weight % 3 == 0
    one_third_weight = total_weight // 3

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
