#!/usr/bin/env python3
import re
from collections import defaultdict


def main():
    transformations, source = load_data()
    print(len(all_possible_transforms(source, transformations)))


def load_data():
    transformations = defaultdict(list)
    with open('19.txt', 'r', encoding='utf-8') as f:
        for line in f:
            l = line.strip()
            if not l:
                continue

            if '=>' in l:
                el_from, chem_to = l.split('=>')
                el_from = el_from.strip()
                chem_to = chemical(chem_to.strip())
                transformations[el_from].append(chem_to)
            else:
                source = chemical(l)
                # Last line in the file
                return transformations, source

def chemical(string):
    return tuple(x for x in re.split(r'([A-Z][a-z]*)', string) if x)


def all_possible_transforms(source, transformations):
    chemicals = set()
    for i, atom in enumerate(source):
        for transformation in transformations[atom]:
            chemicals.add(
                source[:i] + transformation + source[(i + 1):]
            )
    return chemicals



if __name__ == '__main__':
    main()
