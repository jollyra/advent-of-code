#! /usr/bin/env python3


import sys
from util import *


def knot_hash(size, lengths):
    seq = list(range(size))
    skip_size = 0
    i = 0
    for length in lengths:
        sublist = read_wrapping_sublist(seq, length, i)
        write_wrapping_sublist(seq, sublist[::-1], i)
        i = (i + length + skip_size) % size
        skip_size += 1
    return seq[0] * seq[1]


def read_wrapping_sublist(seq, length, i):
    j = i
    sublist = []
    while j < i + length:
        sublist.append(seq[j % len(seq)])
        j += 1
    return sublist


def write_wrapping_sublist(seq, sublist, i):
    for k in range(len(sublist)):
        seq[i % len(seq)] = sublist[k]
        i += 1


if __name__ == '__main__':
    assert(knot_hash(5, [3, 4, 1, 5]) == 12)
    seq = input1_seq('ten_input.txt', ',')
    seq = ints(seq)
    ans = knot_hash(256, seq)
    print('ans', ans)
