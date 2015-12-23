#!/usr/bin/env python3

def main():
    program = load_program()
    execute_and_print_b(program)


def load_program():
    program = []
    with open('23.txt', 'r', encoding='utf-8') as f:
        for line in f:
            name, rest = line.strip().split(' ', 1)
            if ',' in rest:
                rest = tuple(rest.split(','))
            else:
                rest = (rest,)
            program.append((name,) + rest)
    return program


def execute_and_print_b(program):
    i = 0
    registers = {'a': 1, 'b': 0}
    while 0 <= i < len(program):
        instruction = program[i]
        if instruction[0] == 'hlf':
            reg = instruction[1]
            registers[reg] = registers[reg] // 2
        elif instruction[0] == 'tpl':
            reg = instruction[1]
            registers[reg] = registers[reg] * 3
        elif instruction[0] == 'inc':
            reg = instruction[1]
            registers[reg] += 1
        elif instruction[0] == 'jmp':
            distance = int(instruction[1])
            i += distance
            continue
        elif instruction[0] == 'jie':
            reg = instruction[1]
            if registers[reg] % 2 == 0:
                distance = int(instruction[2])
                i += distance
                continue
        elif instruction[0] == 'jio':
            reg = instruction[1]
            if registers[reg] == 1:
                distance = int(instruction[2])
                i += distance
                continue
        i += 1

    print(registers['b'])


if __name__ == '__main__':
    main()
