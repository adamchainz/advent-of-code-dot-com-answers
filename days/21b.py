#!/usr/bin/env python3
import itertools
from collections import namedtuple


def main():
    winning_sets = []
    for equipment_set in possible_equipment_sets():
        boss = Actor(hp=100, damage=8, armour=2)
        player = Actor(
            hp=100,
            damage=sum(i.damage for i in equipment_set),
            armour=sum(i.armour for i in equipment_set),
        )
        if not can_beat(player, boss):
            winning_sets.append(equipment_set)
    print(max(
        sum(i.cost for i in equipment_set)
        for equipment_set in winning_sets
    ))


class Item(object):
    def __init__(self, name, cost, damage, armour):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armour = armour

class Actor(object):
    def __init__(self, hp, damage, armour):
        self.hp = hp
        self.damage = damage
        self.armour = armour

weapons = [
    Item('Dagger', 8, 4, 0),
    Item('Shortsword', 10, 5, 0),
    Item('Warhammer', 25, 6, 0),
    Item('Longsword', 40, 7, 0),
    Item('Greataxe', 74, 8, 0),
]

armours = [
    Item('Leather', 13, 0, 1),
    Item('Chainmail', 31, 0, 2),
    Item('Splintmail', 53, 0, 3),
    Item('Bandedmail', 75, 0, 4),
    Item('Platemail', 102, 0, 5),
]

rings = [
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3),
]

def possible_equipment_sets():
    for weapon_set in possible_weapons():
        for armour_set in possible_armours():
            for ring_set in possible_rings():
                yield weapon_set + armour_set + ring_set

def possible_weapons():
    """
    Exactly one weapon
    """
    for weapon in weapons:
        yield [weapon]


def possible_armours():
    """
    No armour, or one
    """
    yield []
    for armour in armours:
        yield [armour]


def possible_rings():
    """
    0, 1, or 2 individual rings
    """
    yield []
    for ring in rings:
        yield [ring]
    for ring_set in itertools.combinations(rings, 2):
        yield list(ring_set)


def can_beat(player, boss):
    while True:
        boss.hp -= damage(player, boss)
        if boss.hp <= 0:
            return True
        player.hp -= damage(boss, player)
        if player.hp <= 0:
            return False

def damage(actor_a, actor_b):
    return max(1, actor_a.damage - actor_b.armour)


if __name__ == '__main__':
    main()
