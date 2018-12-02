#!/usr/bin/env python3
import json


def main():
    with open('12.json', 'r', encoding='utf-8') as f:
        doc = json.loads(f.read())

    print(sum_of_all_numbers(doc))


def sum_of_all_numbers(doc):
    if isinstance(doc, list):
        return sum(sum_of_all_numbers(x) for x in doc)
    elif isinstance(doc, dict):
        if any(v == "red" for v in doc.values()):
            return 0
        return sum(sum_of_all_numbers(x) for x in doc.values())
    elif isinstance(doc, int):
        return doc
    else:
        return 0


if __name__ == '__main__':
    main()
