#!/usr/bin/env python3


import sys
from collections import deque, defaultdict, namedtuple


def part_one(commands):
    x, y = 0, 0
    visited = set()
    visited.add((x, y))
    for command in list(commands):
        if command == '^':
            y -= 1
        elif command == '>':
            x += 1
        elif command == 'v':
            y += 1
        elif command == '<':
            x -= 1
        visited.add((x, y))
    return len(visited)


def part_two(commands):
    x0, y0 = 0, 0
    x1, y1 = 0, 0
    visited = set()
    visited.add((x0, y0))
    for count, command in enumerate(list(commands)):
        if count % 2 == 0:
            x = x0
            y = y0
        else:
            x = x1
            y = y1
        if command == '^':
            y -= 1
        elif command == '>':
            x += 1
        elif command == 'v':
            y += 1
        elif command == '<':
            x -= 1
        visited.add((x, y))
        if count % 2 == 0:
            x0 = x
            y0 = y
        else:
            x1 = x
            y1 = y
    return len(visited)



def input_line(filename):
    with open(filename, 'r') as f:
        return f.readline().strip()


if __name__ == '__main__':
    assert part_one('>') == 2
    assert part_one('^>v<') == 4
    assert part_one('^v^v^v^v^v') == 2
    assert part_two('^v') == 3
    assert part_two('^>v<') == 3
    assert part_two('^v^v^v^v^v') == 11
    print('pass')

    commands = input_line(sys.argv[1])
    ans = part_one(commands)
    print('ans: {}'.format(ans))
    ans = part_two(commands)
    print('ans: {}'.format(ans))
