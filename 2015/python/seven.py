#!/usr/bin/env python3


def init_circuit(instructions):
    equations = {}
    for ins in instructions:
        if ins[1] == '->':
            in0 = ins[0]
            out = ins[2]
            equations[out] = ['IN', in0]
        elif ins[1] == 'AND':
            in0 = ins[0]
            in1 = ins[2]
            out = ins[4]
            equations[out] = ['AND', in0, in1]
        elif ins[1] == 'OR':
            in0 = ins[0]
            in1 = ins[2]
            out = ins[4]
            equations[out] = ['OR', in0, in1]
        elif ins[1] == 'LSHIFT':
            in0 = ins[0]
            value = int(ins[2])
            out = ins[4]
            equations[out] = ['LSHIFT', in0, value]
        elif ins[1] == 'RSHIFT':
            in0 = ins[0]
            value = int(ins[2])
            out = ins[4]
            equations[out] = ['RSHIFT', in0, value]
        elif ins[0] == 'NOT':
            in0 = ins[1]
            out = ins[3]
            equations[out] = ['NOT', in0]
        else:
            print('oop! unrecognized instruction', ins)
    return equations


def solve(equations, var):
    try:
        return int(var)
    except ValueError:
        pass
    val = equations[var]
    if isinstance(val, int):
        return val
    if not isinstance(val, list):
        return val
    else:
        op, args = val[0], val[1:]
        if op == 'AND':
            ans = solve(equations, args[0]) & solve(equations, args[1])
        elif op == 'OR':
            ans = solve(equations, args[0]) | solve(equations, args[1])
        elif op == 'LSHIFT':
            ans = solve(equations, args[0]) << solve(equations, args[1])
        elif op == 'RSHIFT':
            ans = solve(equations, args[0]) >> solve(equations, args[1])
        elif op == 'NOT':
            ans = (~solve(equations, args[0])) & 0xFFFF
        elif op == 'IN':
            ans = solve(equations, args[0])
        equations[var] = ans
        return ans


def input_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip().split(' ') for line in f]


if __name__ == '__main__':
    instructions = input_lines('7.in')
    equations = init_circuit(instructions)
    for k, v in equations.items():
        print(k, solve(equations, k))
    print('a:', equations['a'])
