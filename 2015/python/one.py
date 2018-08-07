#!/usr/bin/env python3


import sys


def part_one(seq):
    floor = 0
    for i in seq:
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
        else:
            raise ValueError('unrecognized instruction: {}'.format(i))
    return floor


def part_two(seq):
    floor = 0
    for count, i in enumerate(seq, 1):
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
        else:
            raise ValueError('unrecognized instruction: {}'.format(i))
        if floor == -1:
            return count
    return None


def input_line(filename):
    with open(filename, 'r') as f:
        return f.readline().strip()


if __name__ == '__main__':
    assert part_one('(())') == 0
    assert part_one('(()(()(') == 3
    assert part_one('))(((((') == 3
    assert part_two(')') == 1
    assert part_two('()())') == 5
    print('pass')

    instructions = input_line(sys.argv[1])
    a1 = part_one(instructions)
    print('ans part 1: {}'.format(a1))
    a2 = part_two(instructions)
    print('ans part 2: {}'.format(a2))
