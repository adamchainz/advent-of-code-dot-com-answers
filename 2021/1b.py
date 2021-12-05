#!/usr/bin/env python
from itertools import pairwise
from pathlib import Path

from more_itertools import windowed

if __name__ == '__main__':
    readings = [int(x) for x in Path("1.txt").read_text().splitlines()]
    increases = sum(sum(a) < sum(b) for a, b in pairwise(windowed(readings, 3)))
    print(increases)
