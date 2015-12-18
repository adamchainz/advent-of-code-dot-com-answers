#!/usr/bin/env python3

def main():
    presents = []
    with open('2.txt', 'r', encoding='utf-8') as f:
        for line in f:
            l, w, h = line.split('x')
            presents.append((int(l), int(w), int(h)))

    area = 0
    for l, w, h in presents:
        s1 = l * w
        s2 = w * h
        s3 = h * l
        area += (
            2 * s1 +
            2 * s2 +
            2 * s3 +
            min(s1, s2, s3)
        )
    print(area)

if __name__ == '__main__':
    main()
