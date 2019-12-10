#!/usr/bin/env python3
import doctest
import math
from collections import defaultdict
from functools import partial


def input_grid(fn):
    with open(fn, 'r') as f:
        return [line.strip() for line in f]


def render(grid):
    for row in grid:
        print(row)


def asteroids(grid):
    asts = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '#':
                asts.append((x, y))
    return asts


def manhattan_dist(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def angle(src, dst):
    ''' angle returns the angle between src and dst relative to the positive
    x-axis in degrees.
    >>> angle((0, 0), (1, 1))
    45.0
    >>> angle((1, 0), (0, 1))
    135.0
    >>> angle((1, 1), (0, 0))
    225.0
    >>> angle((0, 1), (1, 0))
    315.0
    >>> angle((0, 0), (0, 1))
    90.0
    >>> angle((0, 1), (0, 0))
    270.0
    '''
    dy = dst[1] - src[1]
    dx = dst[0] - src[0]
    if dx == 0 and dy > 0:
        return math.degrees(math.pi / 2)
    if dx == 0 and dy < 0:
        return math.degrees(math.pi * 3 / 2)
    rads = math.atan(dy / dx)
    if dy < 0 and dx < 0:
        rads = math.pi + rads
    if dy >= 0 and dx < 0:
        rads = math.pi + rads
    if dy < 0 and dx >= 0:
        rads = 2*math.pi + rads
    return math.degrees(rads)


def line_of_sight(grid, asts, src):
    manhattan_dist_from_src = partial(manhattan_dist, src)
    sorted_asts = sorted(asts, key=lambda p: manhattan_dist_from_src(p))

    los = defaultdict(list)
    for dst in sorted_asts[1:]:
        los[angle(src, dst)].append(dst)

    return los


def main():
    grid = input_grid('10.in')
    render(grid)
    asts = asteroids(grid)

    loss = {}
    for src in asts:
        loss[src] = (line_of_sight(grid, asts, src))

    detectable_asteroids = defaultdict(int)
    for src, los in loss.items():
        for ds in los.values():
            if len(ds) > 0:
                detectable_asteroids[src] += 1

    print('Part 1', max(detectable_asteroids.values()))



if __name__ == '__main__':
    doctest.testmod()
    main()
