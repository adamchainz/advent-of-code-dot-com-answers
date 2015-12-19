#!/usr/bin/env python3
import re


def main():
    diff = 0
    with open('8.txt', 'r', encoding='utf-8') as f:
        for line in f:
            diff += data_code_diff(line.strip())
    print(diff)


def data_code_diff(string):
    code = '"'
    for char in string:
        if char == '"':
            code += '\\"'
        elif char == '\\':
            code += '\\\\'
        else:
            code += char
    code += '"'
    return len(code) - len(string)


if __name__ == '__main__':
    assert data_code_diff('""') == 4
    assert data_code_diff('"abc"') == 4
    assert data_code_diff('"aaa\\"aaa"') == 6
    assert data_code_diff('"\\x27"') == 5
    main()
