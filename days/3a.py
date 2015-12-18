#!/usr/bin/env python3
from collections import defaultdict


def main():
    with open('3.txt', 'r', encoding='utf-8') as f:
        directions = f.read().strip()

    grid = defaultdict(lambda: defaultdict(int))
    x, y = 0, 0
    grid[x][y] += 1
    for d in directions:
        if d == '>':
            x += 1
        elif d == '<':
            x -= 1
        elif d == '^':
            y -= 1
        elif d == 'v':
            y += 1
        grid[x][y] += 1

    print(sum(len(ys) for ys in grid.values()))

if __name__ == '__main__':
    main()
