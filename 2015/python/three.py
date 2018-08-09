#!/usr/bin/env python3


import sys


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
    santa = [0, 0]
    robosanta = [0, 0]
    visited = set()
    visited.add(tuple(santa))
    cur_santa = santa
    for count, command in enumerate(list(commands)):
        if count % 2 == 0:
            cur_santa = santa
        else:
            cur_santa = robosanta
        if command == '^':
            cur_santa[1] -= 1
        elif command == '>':
            cur_santa[0] += 1
        elif command == 'v':
            cur_santa[1] += 1
        elif command == '<':
            cur_santa[0] -= 1
        visited.add(tuple(cur_santa))
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
