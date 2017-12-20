#! /usr/bin/env python3


import sys
from pprint import pprint
from functools import partial


def traverse(G):
    s = G[0]  # turns out we start at the first non-empty cell we come across
    state = 'down'
    path = [s]
    go = partial(move_if_possible, G)

    while True:
        print(s)
        if state == 'down':
            d = go(down, s)

        elif state == 'up':
            d = go(up, s)

        elif state == 'right':
            d = go(right, s)

        elif state == 'left':
            d = go(left, s)

        print(d)
        if not d:
            return path

        path.append(d)
        s = d


def move_if_possible(G, func, s):
    d = func(s)
    if d in G:
        return d
    else:
        return None


def down(c):
    x, y, v = c
    return (x, y + 1, v)

def up(c):
    x, y, v = c
    return (x, y - 1, v)

def right(c):
    x, y, v = c
    return (x + 1, y, v)

def left(c):
    x, y, v = c
    return (x - 1, y, v)


def Input():
    'Read multiple line separated values'
    with open('19_input.txt', 'r') as f:
        return [line.rstrip() for line in f]


def parse(raw):
    G = []
    for y, row in enumerate(raw):
        for x, cell in enumerate(row):
            if cell is not ' ':
                G.append((x, y, cell))
    return G


if __name__ == '__main__':
    print('')
    raw = Input()
    G = parse(raw)
    pprint(G)
    path = traverse(G)
    print(path)
