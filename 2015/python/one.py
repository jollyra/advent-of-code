#!/usr/bin/env python3


from collections import deque, namedtuple, defaultdict


def part_one(seq):
    floor = 0
    for i in seq:
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
    return floor


def part_two(seq):
    floor = 0
    for count, i in enumerate(seq, 1):
        if i == '(':
            floor += 1
        elif i == ')':
            floor -= 1
        if floor == -1:
            return count
    return None

if __name__ == '__main__':
    assert part_one('(())') == 0
    assert part_one('(()(()(') == 3
    assert part_one('))(((((') == 3
    assert part_two(')') == 1
    print('pass')

    with open('1_input.txt', 'r') as f:
        seq = f.readline().strip()
        a1 = part_one(seq)
        print('ans part 1: {}'.format(a1))
        a2 = part_two(seq)
        print('ans part 2: {}'.format(a2))
