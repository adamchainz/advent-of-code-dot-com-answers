#!/usr/bin/env python
from pathlib import Path

if __name__ == '__main__':
    values = Path("3.txt").read_text().splitlines()

    counts = [0] * len(values[0])
    for value in values:
        for i, bit in enumerate(value):
            if bit == '1':
                counts[i] += 1

    boundary = len(values) // 2
    gamma = int(''.join('1' if i > boundary else '0' for i in counts), 2)
    epsilon = int(''.join('0' if i > boundary else '1' for i in counts), 2)
    print(gamma * epsilon)
