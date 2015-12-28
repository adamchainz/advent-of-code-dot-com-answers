#!/usr/bin/env python3
import itertools
import random
from copy import copy
from functools import partial


def main():
    # example_game_1()
    # example_game_2()
    print(dfs_games(100))


def example_game_1():
    game = Game(
        player=Actor('Player', hp=10, mana=250),
        boss=Actor('Boss', hp=13, damage=8, armour=0),
    )
    print(game)
    game.play([poison])
    print(game)
    try:
        game.play([magic_missile])
    except Lost as e:
        print(e)
    print(game)


def example_game_2():
    game = Game(
        player=Actor('Player', hp=10, mana=250),
        boss=Actor('Boss', hp=14, damage=8, armour=0),
    )
    print(game)
    game.play([recharge])
    print(game)
    game.play([shield])
    print(game)
    game.play([drain])
    print(game)
    game.play([poison])
    print(game)
    try:
        game.play([magic_missile])
    except Lost as e:
        print(e)
    print(game)


def dfs_games(max_depth):
    moves = [magic_missile, drain, shield, poison, recharge]
    best = float('inf')
    best_game = None
    i = 0
    winners = 0

    def search(game, depth):
        nonlocal best_game, i, best, winners

        if depth > max_depth:
            return

        for move in moves:
            if random.random() < 0.0001:
                print(
                    'i = {}, depth = {}, best = {}, winners = {}'
                    .format(i, depth, best, winners)
                )
                if best_game:
                    print(best_game)

            i += 1
            new_game = copy(game)
            try:
                new_game.play([move])
            except Lost as e:
                if e.who is new_game.boss:
                    spent = new_game.player.mana_spent
                    winners += 1
                    if spent < best:
                        best = spent
                        best_game = new_game
                continue
            except IllegalMove:
                continue

            # Prune useless games to recurse
            if new_game.player.mana_spent > best:
                continue

            search(new_game, depth + 1)

    search(Game(), 1)
    print(best_game)
    return best


def bfs_games(max_depth):
    moves = [magic_missile, drain, shield, poison, recharge]

    games = [Game()]
    best = float('inf')
    best_game = None
    depth = 0
    i = 0

    while depth < max_depth:
        depth += 1
        new_games = []
        for game in games:
            for move in moves:
                if random.random() < 0.00001:
                    print(
                        'i = {}, {} games, depth = {}, best = {}'
                        .format(i, len(games), depth, best)
                    )
                    if best_game:
                        print(best_game.moves)

                new_game = copy(game)
                i += 1
                try:
                    new_game.play([move])
                except Lost as e:
                    if e.who is new_game.boss:
                        spent = new_game.player.mana_spent
                        if spent < best:
                            best = spent
                            best_game = new_game
                    continue
                except IllegalMove:
                    continue

                new_games.append(new_game)

        games = new_games

    print(best_game)
    return best


def best_mana_to_win(max_length):
    best = float('inf')
    best_moves = None
    for i, moves in enumerate(all_move_sequences(max_length)):
        game = Game()
        spent = game.mana_spent_if_wins(moves)
        if spent > 0 and spent < best:
            best = spent
            best_moves = moves

        if random.random() < 0.00001:
            print('i = {}, best_cost = {}'.format(i, best))
            print(best_moves)

    return best


def all_move_sequences(max_length):
    moves = [magic_missile, drain, shield, poison, recharge]

    for length in range(1, max_length + 1):
        # generate all sequences of 'length' moves
        movers = [moves] * length
        for m in itertools.product(*movers):
            yield m


class Game(object):
    def __init__(self, boss=None, player=None, moves=None):
        if boss is not None:
            self.boss = boss
        else:
            self.boss = Actor('Boss', hp=55, damage=8, armour=0, mana=0)
        if player is not None:
            self.player = player
        else:
            self.player = Actor('Player', hp=50, damage=0, armour=0, mana=500)
        self.moves = [] if moves is None else moves

    def __str__(self):
        return (
            'Game:\n\t{}\n\t{}\n\tmoves: {}'.format(
                self.boss,
                self.player,
                ', '.join(str(m) for m in self.moves),
            )
        )

    def __copy__(self):
        return Game(
            boss=copy(self.boss),
            player=copy(self.player),
            moves=copy(self.moves)
        )

    def mana_spent_if_wins(self, moves):
        try:
            self.play(moves)
        except Lost as lost:
            if lost.who is self.boss:
                return self.player.mana_spent
            else:
                return 0
        except IllegalMove:
            return 0
        return 0

    def play(self, moves):
        self.moves.extend(moves)
        for move in moves:
            # Player
            self.player.magic_attack(1)  # hard mode
            self.tick()
            move(self)
            # Boss
            self.tick()
            self.player.attack(self.boss.damage)

    def tick(self):
        for actor in (self.boss, self.player):
            actor.tick(self)


class Actor(object):
    def __init__(self, name, hp, damage=0, armour=0, mana=0, effects=None,
                 mana_spent=None):
        self.name = name
        self.hp = hp
        self.damage = damage
        self._base_armour = armour
        self.mana = mana
        self.mana_spent = 0 if mana_spent is None else mana_spent
        self.effects = [] if effects is None else effects

    def __str__(self):
        return (
            '{self.name} (hp={self.hp}, damage={self.damage}, '
            'armour={self.armour}, mana={self.mana}, effects=[{effects}])'
            .format(
                self=self,
                effects=', '.join(str(e) for e in self.effects)
            )
        )

    def __repr__(self):
        return str(self)

    def __copy__(self):
        return Actor(
            name=self.name,
            hp=self.hp,
            damage=self.damage,
            armour=self._base_armour,
            mana=self.mana,
            effects=[copy(e) for e in self.effects],
            mana_spent=self.mana_spent,
        )

    @property
    def armour(self):
        return (
            self._base_armour +
            sum(e.armour_boost for e in self.effects)
        )

    def tick(self, game):
        for effect in self.effects:
            effect.tick(game)
        self.effects = [effect for effect in self.effects
                        if effect.turns_remaining > 0]

    def add_effect(self, effect):
        if any(isinstance(e, effect.__class__) for e in self.effects):
            raise IllegalMove("Cannot re-add {}".format(effect))
        self.effects.append(effect)

    def attack(self, amount):
        damage = max(1, amount - self.armour)
        self.hp -= damage
        if self.hp <= 0:
            raise Lost(self)

    def magic_attack(self, amount):
        self.hp -= amount
        if self.hp <= 0:
            raise Lost(self)

    def heal(self, amount):
        self.hp += amount

    def spend_mana(self, amount):
        if self.mana < amount:
            raise IllegalMove("Not enough mana to spend {}".format(amount))
        self.mana_spent += amount
        self.mana -= amount


class Lost(Exception):
    def __init__(self, who, reason=""):
        self.who = who
        self.reason = reason

    def __str__(self):
        return 'Lost - {}{}'.format(
            self.who,
            ' ' + self.reason if self.reason else ''
        )

    def __repr__(self):
        return str(self).encode('utf-8')


class Spell(object):
    def __init__(self, name, cost, func):
        self.name = name
        self.cost = cost
        self.func = func

    def __str__(self):
        return '{}'.format(self.name)

    def __repr__(self):
        return str(self)

    def __call__(self, game):
        game.player.spend_mana(self.cost)
        self.func(game)


def make_spell(name, cost):
    return partial(Spell, name, cost)


class Effect(object):
    duration = None
    armour_boost = 0

    def __init__(self, turns_remaining=None):
        if turns_remaining is None:
            self.turns_remaining = self.duration
        else:
            self.turns_remaining = turns_remaining

    def __str__(self):
        return '{} ({} turns remaining)'.format(
            self.__class__.__name__,
            self.turns_remaining,
        )

    def __copy__(self):
        return self.__class__(self.turns_remaining)

    def tick(self, game):
        self.turns_remaining -= 1
        self.apply(game)

    def apply(self, game):
        pass


class IllegalMove(Exception):
    pass


# Magic Missile costs 53 mana.
# It instantly does 4 damage.
@make_spell('Magic Missile', 53)
def magic_missile(game):
    game.boss.magic_attack(4)


# Drain costs 73 mana.
# It instantly does 2 damage and heals you for 2 hit points.
@make_spell('Drain', 73)
def drain(game):
    game.boss.magic_attack(2)
    game.player.heal(2)


# Shield costs 113 mana.
# It starts an effect that lasts for 6 turns. While it is active, your armor is
# increased by 7.
@make_spell('Shield', 113)
def shield(game):
    game.player.add_effect(ShieldEffect())


class ShieldEffect(Effect):
    duration = 6
    armour_boost = 7


# Poison costs 173 mana.
# It starts an effect that lasts for 6 turns. At the start of each turn while
# it is active, it deals the boss 3 damage.
@make_spell('Poison', 173)
def poison(game):
    game.boss.add_effect(PoisonEffect())


class PoisonEffect(Effect):
    duration = 6

    def apply(self, game):
        game.boss.magic_attack(3)


# Recharge costs 229 mana.
# It starts an effect that lasts for 5 turns. At the start of each turn while
# it is active, it gives you 101 new mana.
@make_spell('Recharge', 229)
def recharge(game):
    game.player.add_effect(RechargeEffect())


class RechargeEffect(Effect):
    duration = 5

    def apply(self, game):
        game.player.mana += 101

if __name__ == '__main__':
    main()
