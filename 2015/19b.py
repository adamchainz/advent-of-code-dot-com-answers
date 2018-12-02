#!/usr/bin/env python3
import itertools
import operator
import random
import re
from collections import defaultdict
from copy import copy
from functools import reduce


def main():
    transformations, target = load_data()
    print(min_steps_to(target, transformations))


def load_data():
    transformations = []
    with open('19.txt', 'r', encoding='utf-8') as f:
        for line in f:
            l = line.strip()
            if not l:
                continue

            if '=>' in l:
                chem_from, chem_to = l.split('=>')
                chem_from = chemical(chem_from.strip())
                chem_to = chemical(chem_to.strip())
                transformations.append((chem_to, chem_from))
            else:
                target = chemical(l)
                # Last line in the file
                break

    return transformations, target


def chemical(string):
    return tuple(x for x in re.split(r'([A-Z][a-z]*)', string) if x)


def min_steps_to(target, transformations):
    """
    Repeatedly search until we get an answer. Each search is different since it
    uses a different order for transformations.
    """
    steps = 0
    while steps == 0:
        steps = do_min_step_search(target, transformations)
    return steps

def do_min_step_search(target, transformations):
    """
    Perform one search. On each search run we randomly shuffle the
    transformations to avoid any stalemates.
    """
    transformations = copy(transformations)
    random.shuffle(transformations)

    seen = {target}
    class FoundIt(Exception):
        def __init__(self, depth):
            self.depth = depth

    class DidntFindIt(Exception):
        pass

    def search(chem, depth):
        if random.random() <= 0.001:
            print(''.join(chem), depth)
        for chem_to, chem_from in transformations:
            num_replacements, new_chem = apply_reduction_many_times(chem, chem_to, chem_from)
            if new_chem in seen or  num_replacements == 0:
                continue
            elif new_chem == ('e',):
                raise FoundIt(depth + num_replacements)
            else:
                seen.add(new_chem)
                search(new_chem, depth + num_replacements)
        raise Nowt()

    try:
        search(target, 0)
    except FoundIt as e:
        return e.depth
    except DidntFindIt:
        return 0

def apply_reduction_many_times(chem, chem_to, chem_from):
    new_chem = chem
    num = 0
    old_num = 0
    while True:

        for i in range(len(chem) - 1, -1, -1):
            if new_chem[i:i + len(chem_to)] == chem_to:
                num += 1
                new_chem = new_chem[:i] + chem_from + new_chem[i + len(chem_to):]

        if num == old_num:  # no change
            break
        old_num = num

    return num, new_chem


if __name__ == '__main__':
    main()
