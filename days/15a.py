#!/usr/bin/env python3
import operator
from collections import defaultdict, namedtuple
from functools import reduce


def main():
    ingredients = load_ingredients()
    print(max(cookie_scores(ingredients, 100)))


Ingredient = namedtuple('Ingredient', 'name capacity durability flavor texture calories')


def load_ingredients():
    ingredients = []
    with open('15.txt', 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split(' ')
            ingredients.append(Ingredient(
                name=parts[0][:-1],
                capacity=int(parts[2].strip(',')),
                durability=int(parts[4].strip(',')),
                flavor=int(parts[6].strip(',')),
                texture=int(parts[8].strip(',')),
                calories=int(parts[10]),
            ))
    return ingredients


def cookie_scores(ingredients, teaspoons):
    for amounts in lists_summing(len(ingredients), teaspoons):
        totals = defaultdict(int)
        for amount, ingredient in zip(amounts, ingredients):
            for attr in ['capacity', 'durability', 'flavor', 'texture']:
                totals[attr] += amount * getattr(ingredient, attr)
        score = 1
        for t in totals.values():
            score *= max(t, 0)
        yield score


def lists_summing(n, total):
    if n == 1:
        yield [total]
    else:
        for i in range(0, total + 1):
            for sublist in lists_summing(n - 1, total - i):
                yield [i] + sublist


if __name__ == '__main__':
    main()
