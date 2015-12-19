#!/usr/bin/env python3
import re
import operator


def main():
    circuit = {}
    with open('7.txt', 'r', encoding='utf-8') as f:
        for instruction in f:
            add_instruction(circuit, instruction)

    print(get_value(circuit, 'a'))



instruction_re = re.compile(r"""
    (?P<input>
        (?P<input_num>\d+)|
        (?P<input_copy>\w+)|
        (NOT\ (?P<input_not>\w+))|
        (?P<input_operator>
            (?P<input_a>\w+|\d+)
            \ # space
            (?P<input_op>RSHIFT|OR|AND|LSHIFT)
            \ # space
            (?P<input_b>\w+|\d+)
        )
    )
    \ # space
    ->
    \ # space
    (?P<wire>\w+)
""", re.VERBOSE)


def add_instruction(circuit, instruction):
    data = instruction_re.match(instruction.strip()).groupdict()

    wire = data['wire']

    if data['input_num']:
        circuit[wire] = ('num', int(data['input_num']))
    elif data['input_copy']:
        circuit[wire] = ('copy', data['input_copy'])
    elif data['input_not']:
        circuit[wire] = ('not', data['input_not'])
    elif data['input_operator']:
        try:
            a = int(data['input_a'])
        except:
            a = data['input_a']
        try:
            b = int(data['input_b'])
        except:
            b = data['input_b']
        circuit[wire] = ('op', a, data['input_op'], b)
    else:
        import ipdb; ipdb.set_trace()


def get_value(circuit, wire):
    instruction = circuit[wire]
    if instruction[0] == 'num':
        return instruction[1]
    elif instruction[0] == 'copy':
        val = get_value(circuit, instruction[1])
        circuit[wire] = ('num', val)
        return val
    elif instruction[0] == 'not':
        val = get_value(circuit, instruction[1]) ^ 65535
        circuit[wire] = ('num', val)
        return val
    elif instruction[0] == 'op':
        a, op_name, b = instruction[1:]
        if not isinstance(a, int):
            a = get_value(circuit, a)
        if not isinstance(b, int):
            b = get_value(circuit, b)
        val = operators[op_name](a, b) % 65535
        circuit[wire] = ('num', val)
        return val


operators = {
    'RSHIFT': operator.rshift,
    'LSHIFT': operator.lshift,
    'OR': operator.or_,
    'AND': operator.and_,
}

if __name__ == '__main__':
    main()
