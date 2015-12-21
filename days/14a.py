#!/usr/bin/env python3
from collections import namedtuple

def main():
    reindeer = load_reindeer()
    assert furthest_position(reindeer, 1) == max(r.speed for r in reindeer.values())
    print(furthest_position(reindeer, 2503))


class Reindeer(namedtuple('BaseReindeer', 'name speed move_time rest_time')):

    @property
    def cycle_time(self):
        return self.move_time + self.rest_time


def load_reindeer():
    reindeer = {}
    with open('14.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split()
            reindeer[parts[0]] = Reindeer(
                name=parts[0],
                speed=int(parts[3]),
                move_time=int(parts[6]),
                rest_time=int(parts[-2]),
            )
    return reindeer


def furthest_position(reindeer, duration):
    positions = {name: 0 for name in reindeer}

    for t in range(1, duration + 1):
        for deer in reindeer.values():
            tr = t % deer.cycle_time
            if tr == 0:
                tr = deer.cycle_time
            if tr <= deer.move_time:
                positions[deer.name] += deer.speed
    return max(positions.values())

if __name__ == '__main__':
    main()
