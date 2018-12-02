#!/usr/bin/env python3
from collections import defaultdict


def main():
    grid = load_grid()

    for step in range(100):
        grid = evolve(grid)

    n = 0
    for y in range(100):
        for x in range(100):
            n += int(grid[y][x])
    print(n)


def load_grid():
    grid = defaultdict(lambda: defaultdict(int))
    with open('18.txt', 'r', encoding='utf-8') as f:
        for y, line in enumerate(f):
            for x, state in enumerate(line.strip()):
                if state == '#':
                    grid[y][x] = True
    # corners always on
    grid[0][0] = True
    grid[99][0] = True
    grid[99][99] = True
    grid[0][99] = True
    return grid


def evolve(grid):
    new_grid = defaultdict(lambda: defaultdict(int))
    for y in range(100):
        for x in range(100):
            neighbours_on = 0
            if y - 1 >= 0:
                if x - 1 >= 0 and grid[y - 1][x - 1]:
                    neighbours_on += 1
                if grid[y - 1][x]:
                    neighbours_on += 1
                if x + 1 < 100 and grid[y - 1][x + 1]:
                    neighbours_on += 1

            if x - 1 >= 0 and grid[y][x - 1]:
                neighbours_on += 1
            if x + 1 < 100 and grid[y][x + 1]:
                neighbours_on += 1

            if y + 1 < 100:
                if x - 1 >= 0 and grid[y + 1][x - 1]:
                    neighbours_on += 1
                if grid[y + 1][x]:
                    neighbours_on += 1
                if x + 1 < 100 and grid[y + 1][x + 1]:
                    neighbours_on += 1


            if grid[y][x]:
                new_grid[y][x] = (neighbours_on in (2, 3))
            else:
                new_grid[y][x] = (neighbours_on == 3)

    # corners always on
    new_grid[0][0] = True
    new_grid[99][0] = True
    new_grid[99][99] = True
    new_grid[0][99] = True

    return new_grid

if __name__ == '__main__':
    main()
