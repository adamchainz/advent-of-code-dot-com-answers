#!/usr/bin/env python
from pathlib import Path

if __name__ == '__main__':
    lines = Path("2.txt").read_text().splitlines()

    aim = 0
    horizontal = 0
    depth = 0
    for line in lines:
        command, value_str = line.split(' ')
        value = int(value_str)
        if command == 'forward':
            horizontal += value
            depth += aim * value
        elif command == 'down':
            aim += value
        elif command == 'up':
            aim -= value

    print(horizontal * depth)
