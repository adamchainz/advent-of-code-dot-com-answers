#!/usr/bin/env python
from itertools import pairwise
from pathlib import Path

if __name__ == '__main__':
    readings = [int(x) for x in Path("1.txt").read_text().splitlines()]
    increases = sum(a < b for a, b in pairwise(readings))
    print(increases)
