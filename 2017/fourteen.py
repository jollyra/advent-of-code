#! /usr/bin/env python3


from knot_hash import hash
from util import *
from functools import partial


def count_regions(M):
    count = 0
    used_cells = find_used_cells(M)
    visited = set()
    unvisited = used_cells - visited
    while unvisited:
        p = unvisited.pop()
        region = explore_region(M, p)
        visited |= region
        count += 1
        unvisited = used_cells - visited
    return count


def explore_region(M, p):
    visited = set()
    horizon = [p]
    while len(horizon):
        p = horizon.pop()
        visited.add(p)
        neighbours = filter(partial(is_in_range, len(M)), neighbours4(p))
        horizon.extend([n for n in neighbours if M[Y(n)][X(n)] == '1' and n not in visited])
    return visited


def is_in_range(size, p):
    return X(p) >= 0 and X(p) < size and Y(p) >= 0 and Y(p) < size



def find_used_cells(M):
    used_cells = set()
    for y in range(len(M)):
        for x in range(len(M)):
            if M[y][x] == '1':
                used_cells.add((x, y))
    return used_cells


def count_used_squares(M):
    count = 0
    for row in M:
        for cell in row:
            if cell == '1':
                count += 1
    return count


def decrypt_disk(string):
    key_strings = []
    for n in range(128):
        key_string = '{}-{}'.format(string, n)
        key_strings.append(key_string)
    hashes = [hash(s) for s in key_strings]
    bins = [hexstring_to_binary(h) for h in hashes]
    return bins


def hexstring_to_binary(hexs):
    ints = [int(x, 16) for x in hexs]
    bins = [format(i, 'b').zfill(4) for i in ints]
    binarystring = ''.join(bins)
    assert(len(binarystring) == 4 * len(hexs))
    return binarystring


if __name__ == '__main__':
    M = decrypt_disk('hfdlxzhv')
    num_used_squares = count_used_squares(M)
    assert(num_used_squares == 8230)
    print('Memory used:', num_used_squares)
    num_regions = count_regions(M)
    print('Regions:', num_regions)
