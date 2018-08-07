#!/usr/bin/env python3


import sys
from collections import deque, defaultdict, namedtuple


def calculate_wrapping_paper_needed(l, w, h):
    face1, face2, face3 = l * w, w * h, h * l
    smallest_face = min(face1, face2, face3)
    return 2 * face1 + 2 * face2 + 2 * face3 + smallest_face


def calculate_ribbon_needed(l, w, h):
    perimeter1 = 2 * l + 2 * w
    perimeter2 = 2 * w + 2 * h
    perimeter3 = 2 * h + 2 * l
    smallest_perimeter = min(perimeter1, perimeter2, perimeter3)
    volume = l * w * h
    return smallest_perimeter + volume


def input_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]


def parse_input(lines):
    boxes = []
    for line in lines:
        box_dimensions = [int(d) for d in line.split('x')]
        boxes.append(box_dimensions)
    return boxes


if __name__ == '__main__':
    assert calculate_wrapping_paper_needed(2, 3, 4) == 58
    assert calculate_ribbon_needed(2, 3, 4) == 34
    print('pass')

    lines = parse_input(input_lines(sys.argv[1]))
    total_wrapping = 0
    total_ribbon = 0
    for line in lines:
        total_wrapping += calculate_wrapping_paper_needed(*line)
        total_ribbon += calculate_ribbon_needed(*line)
    print('square feet of wrapping paper: {}'.format(total_wrapping))
    print('feet of ribbon: {}'.format(total_ribbon))
