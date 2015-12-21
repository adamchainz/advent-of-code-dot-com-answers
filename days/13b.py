#!/usr/bin/env python3
from collections import defaultdict
from itertools import permutations


def main():
    matrix = load_matrix()
    print(max(
        total_happiness(arrangement, matrix)
        for arrangement in permutations(list(matrix.keys()))
    ))


def load_matrix():
    matrix = defaultdict(lambda: defaultdict(int))
    with open('13.txt', 'r', encoding='utf-8') as f:
        for line in f:
            source, _, sign, n, _, _, _, _, _, _, destination = line.split()
            amount = (1 if sign == 'gain' else -1) * int(n)
            destination = destination[:-1]  # remove .
            matrix[source][destination] = amount

    # Add self
    for source in matrix:
        matrix[source]['Me'] = 0
    matrix['Me'] = {destination: 0 for destination in matrix.keys()}

    return matrix


def total_happiness(arrangement, matrix):
    happiness = 0
    for i, name in enumerate(arrangement):
        right = arrangement[(i + 1) % len(arrangement)]
        happiness += matrix[name][right]
        left = arrangement[(i - 1) % len(arrangement)]
        happiness += matrix[name][left]
    return happiness


if __name__ == '__main__':
    main()
