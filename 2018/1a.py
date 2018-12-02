#!/usr/bin/env python
def main():
    with open('1.txt', 'r') as fp:
        lines = fp.readlines()
    frequency_changes = [int(x) for x in lines]
    print(sum(frequency_changes))


if __name__ == '__main__':
    main()
