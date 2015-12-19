#!/usr/bin/env python3
import re


def main():
    diff = 0
    with open('8.txt', 'r', encoding='utf-8') as f:
        for line in f:
            diff += code_data_diff(line.strip())
    print(diff)

def code_data_diff(string):
    data = ""
    i = 1
    while i < len(string) - 1:  # ignoring quotes
        if string[i] == '\\':
            if string[i + 1] == '\\':
                data += '\\'
                i += 2
                continue
            elif string[i + 1] == '"':
                data += '"'
                i += 2
                continue
            elif string[i + 1] == 'x' and is_hex(string[i + 2]) and is_hex(string[i + 3]):
                data += 'X'
                i += 4
                continue
            else:
                raise ValueError("Invalid escape sequence: " + string[i: i + 4])
        else:
            data += string[i]
            i += 1
    return len(string) - len(data)


def is_hex(char):
    return char in '0123456789abcdef'


if __name__ == '__main__':
    assert code_data_diff('""') == 2
    assert code_data_diff('"abc"') == 2
    assert code_data_diff('"aaa\\"aaa"') == 3
    assert code_data_diff('"azlgxdbljwygyttzkfwuxv"') == 2
    assert code_data_diff('"\\x27"') == 5
    assert code_data_diff('"\\x27"') == 5
    main()
