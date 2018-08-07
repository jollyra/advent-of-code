#!/usr/bin/env python3


import sys
from collections import deque, defaultdict, namedtuple


def calculate_wrapping_paper_needed(l, w, h):
    a1, a2, a3 = l * w, w * h, h * l
    smallest = min(a1, a2, a3)
    return 2 * a1 + 2 * a2 + 2 * a3 + smallest


def calculate_ribbon_needed(l, w, h):
    p1 = 2 * l + 2 * w
    p2 = 2 * w + 2 * h
    p3 = 2 * h + 2 * l
    smallest = min(p1, p2, p3)
    volume = l * w * h
    return smallest + volume


def input_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def parse_input(lines):
    boxes = []
    for line in lines:
        dimensions = line.split('x')
        dimensions = [int(d) for d in dimensions]
        boxes.append(dimensions)
    return boxes


if __name__ == '__main__':
    assert calculate_wrapping_paper_needed(2, 3, 4) == 58
    assert calculate_ribbon_needed(2, 3, 4) == 34
    print('pass')

    lines = input_lines(sys.argv[1])
    lines = parse_input(lines)
    total_wrapping = 0
    total_ribbon = 0
    for line in lines:
        total_wrapping += calculate_wrapping_paper_needed(*line)
        total_ribbon += calculate_ribbon_needed(*line)
    print('ans part 1: {}'.format(total_wrapping))
    print('ans part 2: {}'.format(total_ribbon))
