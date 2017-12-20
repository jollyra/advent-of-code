#! /usr/bin/env python3


import sys
from pprint import pprint
from functools import partial
from util import trace, cat


def traverse(G):
    p = get_start(G)
    state = 'south'
    path = []
    while True:
        print(p)

        if G[p] == '+':
            state = get_next_direction(G, p, path[-1])

        path.append(p)
        p = next_point(state, p)
        if not G.get(p):
            return path


def next_point(state, p):
    x, y = p
    if state == 'south':
        return (x, y + 1)
    elif state == 'north':
        return (x, y - 1)
    elif state == 'east':
        return (x + 1, y)
    elif state == 'west':
        return (x - 1, y)


def get_next_direction(G, p, prev_p):
    nays = neighbours4(p)
    print(nays)
    del nays[prev_p]
    for p, state in nays.items():
        print(p, state)
        if G.get(p):
            return state


def neighbours4(point):
    x, y = point
    return {(x + 1, y): 'east', (x, y + 1): 'south', (x - 1, y): 'west', (x, y - 1): 'north'}


def get_start(G):
    for c in G:
        x, y = c
        if y == 0:
            return c

def Input():
    'Read multiple line separated values'
    with open('19_input.txt', 'r') as f:
        return [line.rstrip() for line in f]


def parse(raw):
    G = {}
    for y, row in enumerate(raw):
        for x, cell in enumerate(row):
            if cell is not ' ':
                G[(x, y)] = cell
    return G


if __name__ == '__main__':
    raw = Input()
    G = parse(raw)
    path = traverse(G)
    letters = cat([G[c] for c in path if G[c].isalpha()])
    print('Part A: {} - Letters seen'.format(letters))
    print('Part B: {} - No. of steps'.format(len(path)))
