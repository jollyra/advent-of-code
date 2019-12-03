#!/usr/bin/env python3


def input_seqs(filename, sep=None):
    seqs = []
    with open(filename, 'r') as f:
        for line in f:
            seqs.append([el for el in line.strip().split(sep)])
    return seqs


def add_points(p, q):
    return p[0] + q[0], p[1] + q[1]


def manhattan_distance(p, q):
    return (abs(X(p) - X(q)) + abs(Y(p) - Y(q)))


cardinals = {
    'R': (1, 0),
    'U': (0, 1),
    'L': (-1, 0),
    'D': (0, -1),
}


def trace_path(ds):
    cur = (0, 0)
    path = [cur]
    for d in ds:
        direction = d[0]
        vec = cardinals[direction]
        steps = int(d[1:])
        for _ in range(steps):
            cur = add_points(cur, vec)
            path.append(cur)

    return path


def find_intersects(w1, w2):
    s1, s2 = set(w1[1:]), set()
    intersects = []
    for p in w2[1:]:
        if p in s1:
            intersects.append(p)
        s2.add(p)
    return intersects


def main():
    print('pass')
    wires = input_seqs('3.in', ',')
    wire_paths = [trace_path(d) for d in wires]
    intersections = find_intersects(*wire_paths)
    dists_to_intersections = [manhattan_distance(i, (0, 0)) for i in intersections]
    print('Part 1:', min(dists_to_intersections))

    steps_to_intersection = []
    for intersect in intersections:
        j = wire_paths[0].index(intersect)
        k = wire_paths[1].index(intersect)
        steps_to_intersection.append(j + k)
    print('Part 2:', min(steps_to_intersection))


if __name__ == '__main__':
    main()
