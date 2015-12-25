#!/usr/bin/env python3
import itertools
import random


def main():
    assert grid_n(1, 1) == 1
    assert grid_n(1, 2) == 2
    assert grid_n(2, 1) == 3
    assert grid_n(2, 2) == 5
    assert grid_n(1, 4) == 7
    assert grid_n(4, 2) == 14
    assert code(1, 1) == 20151125
    assert code(1, 2) == 31916031
    assert code(2, 1) == 18749137
    assert code(2, 2) == 21629792
    assert code(3, 5) == 28094349
    desired_grid = (3083, 2978)
    print(code(*desired_grid))


def grid_n(x, y):
    n = x + y - 1
    return int(
        (n ** 2) -
        ((n ** 2 - n) / 2) -
        y +
        1
    )


def code(x, y):
    times = pow(252533, grid_n(x, y) - 1, 33554393)
    return (20151125 * times) % 33554393


if __name__ == '__main__':
    main()
