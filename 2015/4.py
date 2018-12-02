#!/usr/bin/env python3
from hashlib import md5
from itertools import count


def main():
    key = b"ckczppom"
    for i in count(start=1):
        h = md5(key + str(i).encode('ascii')).hexdigest()
        if h.startswith('000000'):
            print(i, h)
            break
        if i % 1000000 == 0:
            print(i)

if __name__ == '__main__':
    main()
