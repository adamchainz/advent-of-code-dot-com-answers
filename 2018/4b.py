#!/usr/bin/env python
import datetime as dt
import re
from collections import defaultdict, namedtuple
from enum import Enum

Observation = namedtuple('Observation', ['when', 'type', 'guard_id'])
ObservationType = Enum('ObservationType', ['BEGINS_SHIFT', 'FALLS_ASLEEP', 'WAKES_UP'])
observation_re = re.compile(
    r'^\[(?P<y>\d+)-(?P<m>\d+)-(?P<d>\d+) (?P<h>\d+):(?P<min>\d+)\] (?P<type>Guard #(?P<guard_id>\d+) begins shift|falls asleep|wakes up)$',
)


def main():
    observations = load_observations()

    minutes_guards_asleep = defaultdict(lambda: defaultdict(int))
    current_guard_id = None
    sleep_start_minute = None
    for observation in observations:
        if observation.type == ObservationType.BEGINS_SHIFT:
            current_guard_id = observation.guard_id
        elif observation.type == ObservationType.FALLS_ASLEEP:
            sleep_start_minute = observation.when.minute
        elif observation.type == ObservationType.WAKES_UP:
            for minute in range(sleep_start_minute, observation.when.minute):
                minutes_guards_asleep[minute][current_guard_id] += 1

    minutes_asleep, guard_id, minute = max(
        (minutes_asleep, guard_id, minute)
        for minute, entries in minutes_guards_asleep.items()
        for guard_id, minutes_asleep in entries.items()
    )
    print(minute * guard_id)


def load_observations():
    observations = []
    with open('4.txt', 'r') as fp:
        for line in fp.readlines():
            groups = observation_re.match(line)
            if not groups:
                raise ValueError(f"Didn't match {repr(line)}")

            when = dt.datetime(
                year=int(groups['y']),
                month=int(groups['m']),
                day=int(groups['d']),
                hour=int(groups['h']),
                minute=int(groups['min']),
            )
            if groups['type'].startswith('Guard'):
                type_ = ObservationType.BEGINS_SHIFT
                guard_id = int(groups['guard_id'])
            elif groups['type'] == 'falls asleep':
                type_ = ObservationType.FALLS_ASLEEP
                guard_id = None
            elif groups['type'] == 'wakes up':
                type_ = ObservationType.WAKES_UP
                guard_id = None
            observations.append(Observation(
                when=when,
                type=type_,
                guard_id=guard_id,
            ))
    observations.sort(key=lambda o: o.when)
    return observations


if __name__ == '__main__':
    main()
