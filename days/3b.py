#!/usr/bin/env python3
from collections import defaultdict


def main():
    with open('3.txt', 'r', encoding='utf-8') as f:
        directions = f.read().strip()

    grid = defaultdict(lambda: defaultdict(int))
    santa = Santa(grid)
    robosanta = Santa(grid)

    di = iter(directions)
    for d1, d2 in zip(di, di):
        santa.move(d1)
        robosanta.move(d2)
    print(sum(len(ys) for ys in grid.values()))


class Santa(object):
    def __init__(self, grid):
        self.grid = grid
        self.x = 0
        self.y = 0
        self.grid[self.x][self.y] += 1

    def move(self, d):
        if d == '>':
            self.x += 1
        elif d == '<':
            self.x -= 1
        elif d == '^':
            self.y -= 1
        elif d == 'v':
            self.y += 1
        self.grid[self.x][self.y] += 1


if __name__ == '__main__':
    main()
