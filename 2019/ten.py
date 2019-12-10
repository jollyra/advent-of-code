#!/usr/bin/env python3
import doctest
import math
from collections import defaultdict, deque
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


def best_asteroid_for_station(lines):
    detectable_asteroids = defaultdict(int)
    for src, los in lines.items():
        for ds in los.values():
            if len(ds) > 0:
                detectable_asteroids[src] += 1
    station = max(detectable_asteroids.keys(), key=lambda k:detectable_asteroids[k])
    nastroids = detectable_asteroids[station]
    return station, nastroids


def vaporized_order(los, station):
    i = 0
    layers = []
    while True:
        layer = deque()
        for line in los.values():
            if len(line) > i:
                layer.append(line[i])
        if len(layer) == 0:
            break
        layers.append(layer)
        i += 1

    vaporized = []
    angle_from_station = partial(angle, station)
    for l ,layer in enumerate(layers):
        clockwise_layer = deque(sorted(layer, key=angle_from_station))
        for j in range(len(clockwise_layer)):
            if angle_from_station(clockwise_layer[0]) >= 270.0:
                break
            clockwise_layer.rotate(-1)
        assert(len(clockwise_layer) == len(layer))
        for ast in clockwise_layer:
            vaporized.append(ast)
            # print(l, num_vaporized, ast, angle_from_station(ast))

    return vaporized

def main():
    grid = input_grid('10.in')
    asts = asteroids(grid)
    lines = {src: line_of_sight(grid, asts, src) for src in asts}

    station, nastroids = best_asteroid_for_station(lines)
    assert(nastroids == 314)
    print(f'Part 1: build a station at {station} that sees {nastroids} asteroids')

    # grid = input_grid('10_test_part2.in')
    # grid = input_grid('10_test2.in')
    grid = input_grid('10.in')
    asts = asteroids(grid)
    lines = {src: line_of_sight(grid, asts, src) for src in asts}
    station, nastroids = best_asteroid_for_station(lines)
    print(f'Part 2: build a station at {station} that sees {nastroids} asteroids')

    vaporized = vaporized_order(lines[station], station)
    for i, v in enumerate(vaporized, start=1):
        print(i, v)





if __name__ == '__main__':
    doctest.testmod()
    main()
