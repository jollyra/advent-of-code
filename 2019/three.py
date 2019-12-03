#!/usr/bin/env python3


def input_seqs(filename):
    seqs = []
    with open(filename, 'r') as f:
        for line in f:
            seqs.append([el for el in line.split(',')])
    return seqs


def manhattan_distance(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def trace_path(directions):
    cardinals = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1),}
    cur = (0, 0)
    path = [cur]
    for d in directions:
        direction = d[0]
        vec = cardinals[direction]
        steps = int(d[1:])
        for _ in range(steps):
            cur = cur[0] + vec[0], cur[1] + vec[1]
            path.append(cur)
    return path


def find_intersections(w1, w2):
    return set(w1[1:]) & set(w2[1:])


def closest_intersection(intersections):
    return min(manhattan_distance(i, (0, 0)) for i in intersections)


def fastest_intersection(wire_paths, intersections):
    steps_to_intersection = []
    for intersect in intersections:
        j = wire_paths[0].index(intersect)
        k = wire_paths[1].index(intersect)
        steps_to_intersection.append(j + k)
    return min(steps_to_intersection)


if __name__ == '__main__':
    wires = input_seqs('3.in')
    wire_paths = [trace_path(d) for d in wires]
    intersections = find_intersections(*wire_paths)
    print('Part 1:', closest_intersection(intersections))
    print('Part 2:', fastest_intersection(wire_paths, intersections))
