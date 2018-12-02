#!/usr/bin/env python3

def main():
    containers = load_containers()
    combos = list(combinations_summing(containers, 150))
    min_length = min(len(c) for c in combos)
    minima = [c for c in combos if len(c) == min_length]
    print(len(minima))


def load_containers():
    containers = []
    with open('17.txt', 'r', encoding='utf-8') as f:
        for line in f:
            containers.append(int(line.strip()))
    return tuple(containers)


def combinations_summing(containers, litres):
    if not len(containers) or sum(containers) < litres:
        return

    container, others = containers[0], containers[1:]
    if container == litres:
        yield [container]
    elif container < litres:
        for other_combo in combinations_summing(others, litres - container):
            yield [container] + other_combo

    for other_combo in combinations_summing(others, litres):
        yield other_combo

if __name__ == '__main__':
    main()
