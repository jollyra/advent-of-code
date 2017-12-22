#! /usr/bin/env python3


def virus(G, p, iterations):
    direction = (0, -1)
    infected = 0
    for i in range(iterations):
        cell = G.setdefault(p, '.')
        if cell == '#':
            direction = rotate(direction, 'R')
            G[p] = 'F'
        elif cell == '.':
            direction = rotate(direction, 'L')
            G[p] = 'W'
        elif cell == 'W':
            G[p] = '#'
            infected += 1
        elif cell == 'F':
            direction = rotate(direction, 'L')
            direction = rotate(direction, 'L')
            G[p] = '.'
        p = add(p, direction)
    return infected


def add(a, b):
    xa, ya = a
    xb, yb = b
    return (xa + xb, ya + yb)


def rotate(v, rotation):
    return (-v[1], v[0]) if rotation == 'R' else (v[1], -v[0])


def get_start(raw):
    y = len(raw) // 2
    x = len(raw[0]) // 2
    return (x, y)


def parse(seqs):
    G = {}
    for y in range(len(seqs)):
        for x in range(len(seqs[y])):
            G[(x, y)] = seqs[y][x]
    return G


def Input():
    with open('22_input.txt', 'r') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    raw = Input()
    start_point = get_start(raw)
    G = parse(raw)
    infected_count = virus(G, start_point, 10000000)
    print(f'Virus infected {infected_count} nodes')
