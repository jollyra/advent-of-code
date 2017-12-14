#! /usr/bin/env python3

import util
import numpy as np
import re


def rotateNegative90(A):
    'turn right'
    A = np.array(A)
    B = np.array([[0, -1],
                  [1, 0]])
    return A.dot(B)


def rotatePositive90(A):
    'turn left'
    A = np.array(A)
    B = np.array([[0, 1],
                  [-1, 0]])
    return A.dot(B)


def parse(directions):
    directions = directions.split(', ')
    parsed = []
    for direction in directions:
        turn, dist = re.search(r'([A-Z])([0-9]+)', direction).groups()
        parsed.append((turn, int(dist)))
    return parsed


def how_far(directions):
    heading = np.array([0, 1])
    position = np.array([0, 0])
    for (turn, dist) in parse(directions):
        if turn == 'L':
            heading = rotatePositive90(heading)
        elif turn == 'R':
            heading = rotateNegative90(heading)
        position += heading * dist
    return util.manhattan_distance((0, 0), position.tolist())


def main():
    assert how_far('R2, L3') == 5
    assert how_far('R2, R2, R2') == 2
    assert how_far('R5, L5, R5, R3') == 12

    with open('one_input.txt', 'r') as f:
        directions = f.read()
        distance = how_far(directions)
        print(distance)


if __name__ == '__main__':
    main()
