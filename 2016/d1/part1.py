#! /usr/bin/env python3

import util
import numpy as np


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


# TODO: this should use regex
def parse(directions):
    directions = directions.split(',')
    parsed = []
    for direction in directions:
        direction = direction.strip()
        turn = direction[0]
        rest = ''.join(direction[1:])
        dist = int(rest)
        parsed.append((turn, dist))
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

    directions = input().strip()
    distance = how_far(directions)
    print(distance)


if __name__ == '__main__':
    main()
