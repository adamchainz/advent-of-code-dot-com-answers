#!/usr/bin/env python3

def main():
    presents = []
    with open('2.txt', 'r', encoding='utf-8') as f:
        for line in f:
            l, w, h = line.split('x')
            presents.append((int(l), int(w), int(h)))

    ribbon = 0
    for l, w, h in presents:
        p1 = 2 * l + 2 * w
        p2 = 2 * w + 2 * h
        p3 = 2 * h + 2 * l

        wrap_ribbon = min((p1, p2, p3))
        bow_ribbon = l * w * h
        ribbon += wrap_ribbon + bow_ribbon
    print(ribbon)

if __name__ == '__main__':
    main()
