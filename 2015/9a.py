#!/usr/bin/env python3
import re
from collections import defaultdict
from copy import deepcopy


def main():
    distances = defaultdict(lambda: defaultdict(int))

    with open('9.txt', 'r', encoding='utf-8') as f:
        for line in f:
            add_distance(distances, line)

    print(shortest_route(distances))


distance_re = re.compile(r'''
    (?P<source>\w+)
    \ to \ # space
    (?P<destination>\w+)
    \ = \ #  space
    (?P<distance>\d+)
''', re.VERBOSE)


def add_distance(distances, line):
    match = distance_re.match(line.strip()).groupdict()
    distances[match['source']][match['destination']] = int(match['distance'])
    distances[match['destination']][match['source']] = int(match['distance'])


def shortest_route(distances):
    return min(
        shortest_route_from(deepcopy(distances), location)
        for location in distances
    )


def shortest_route_from(distances, source):
    # Remove current position from grid
    current_distances = distances.pop(source)
    for destination in distances:
        del distances[destination][source]

    # Base case
    if not distances:
        return 0

    # Recursive
    best = float('inf')
    for destination in distances:
        total_distance = (
            current_distances[destination] +
            shortest_route_from(deepcopy(distances), destination)
        )
        best = min(best, total_distance)
    return best


if __name__ == '__main__':
    main()
