#!/usr/bin/env python
def main():
    with open('1.txt', 'r') as fp:
        lines = fp.readlines()
    frequency_changes = [int(x) for x in lines]
    print(first_repeated_frequency(frequency_changes))


def first_repeated_frequency(frequency_changes):
    seen_frequencies = set()
    frequency = 0
    while True:
        for frequency_change in frequency_changes:
            seen_frequencies.add(frequency)
            frequency += frequency_change
            if frequency in seen_frequencies:
                return frequency


if __name__ == '__main__':
    main()
