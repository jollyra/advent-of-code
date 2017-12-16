#! /usr/bin/env python3


from collections import deque
from util import *


cat = ''.join


def find_period(seq, moves, rounds):
    seq = deque(seq)
    cache = set()
    for i in range(rounds):
        seq = dance(seq, moves)
        if cat(seq) in cache:
            print('repeat!', cat(seq), i)
            return i
        else:
            cache.add(cat(seq))
    return cat(seq)


def dance(seq, moves):
    for move in moves:
        if move[0] == 's':
            seq.rotate(int(move[1:]))
        elif move[0] == 'x':
            a, b = move[1:].split('/')
            a, b = (int(a), int(b))
            seq[b], seq[a] = seq[a], seq[b]
        elif move[0] == 'p':
            a, b = move[1:].split('/')
            ia, ib = (seq.index(a), seq.index(b))
            ia, ib = (int(ia), int(ib))
            seq[ib], seq[ia] = seq[ia], seq[ib]
    return seq


if __name__ == '__main__':
    letters = 'abcdefghijklmnop'
    one_billion = int(1e9)
    moves = input1_seq(f='16', sep=',')
    period = find_period(letters, moves, one_billion)
    i = (one_billion % period)
    seq = find_period(letters, moves, i)
    print('Letters look like {} after 1 billion rounds of dance'.format(seq))
