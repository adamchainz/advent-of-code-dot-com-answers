#!/usr/bin/env python3
import re

def main():
    grid = make_grid(1000)
    with open('6.txt', 'r', encoding='utf-8') as f:
        for instruction in f:
            update_grid(grid, instruction.strip())
    print(num_on(grid))


def make_grid(size):
    return [
        [False for i in range(size)]
        for i in range(size)
    ]


def num_on(grid):
    n = 0
    for line in grid:
        for p in line:
            if p:
                n += 1
    return n


instruction_re = re.compile(r"""
    (?P<func>toggle|turn\ off|turn\ on)
    \ # space
    (?P<x1>\d+),(?P<y1>\d+)
    \ through\ # space
    (?P<x2>\d+),(?P<y2>\d+)
""", re.VERBOSE)

def update_grid(grid, instruction):
    data = instruction_re.match(instruction).groupdict()
    func = data['func']
    x1, y1 = int(data['x1']), int(data['y1'])
    x2, y2 = int(data['x2']), int(data['y2'])

    if data['func'] == 'toggle':
        def mutate(v):
            return not v
    elif data['func'] == 'turn off':
        def mutate(v):
            return False
    elif data['func'] == 'turn on':
        def mutate(v):
            return True

    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if func == 'turn off':
                grid[x][y] = False
            elif func == 'turn on':
                grid[x][y] = True
            elif func == 'toggle':
                grid[x][y] = not grid[x][y]


if __name__ == '__main__':
    main()
