#! /usr/bin/env python3


from collections import deque
from util import *


cat = ''.join


def find_first_cycle(ps, moves):
    ps = deque(ps)
    cache = set()
    for i in range(1000000000):
        ps = dance(ps, moves)
        if cat(ps) in cache:
            print('repeat!', cat(ps), i)
            return 'win'
        else:
            cache.add(cat(ps))
    return cat(ps)


def dance(ps, moves):
    for move in moves:
        if move[0] == 's':
            ps.rotate(int(move[1:]))
        elif move[0] == 'x':
            args = move[1:].split('/')
            a = int(args[0])
            b = int(args[1])
            ps[b], ps[a] = ps[a], ps[b]
        elif move[0] == 'p':
            args = move[1:].split('/')
            a = ps.index(args[0])
            b = ps.index(args[1])
            ps[b], ps[a] = ps[a], ps[b]
    return ps


if __name__ == '__main__':
    letters = 'abcdefghijklmnop'
    moves = input1_seq(f='16', sep=',')
    find_first_cycle(letters, moves)
