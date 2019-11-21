from util import *
from collections import defaultdict


def neighbours_diagonal(point):
    'Only diagonals returned in order quadrants I, II, III, IV (CCW).'
    x, y = point
    return [(x + 1, y + 1), (x - 1, y + 1), (x - 1, y - 1), (x + 1, y - 1)]


def east(point):
    x, y = point
    return (x + 1, y)


def north(point):
    x, y = point
    return (x, y + 1)


def west(point):
    x, y = point
    return (x - 1, y)


def south(point):
    x, y = point
    return (x, y - 1)


def bounds(m):
    x_min = x_max = y_min = y_max = 0
    for p in m:
        x_max = max(x_max, X(p))
        x_min = min(x_min, X(p))
        y_max = max(y_max, Y(p))
        y_min = min(y_min, Y(p))
    return x_min, x_max, y_min, y_max


def fill_unknowns_with_walls(m):
    x_min, x_max, y_min, y_max = bounds(m)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            p = (x, y)
            if p not in m:
                m[p] = '#'


def render_map(m):
    x_min, x_max, y_min, y_max = bounds(m)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            p = (x, y)
            if p in m:
                print(m[p], end='')
            else:
                print('?', end='')
        print()


def find_current_location(m):
    for p, tile in m.items():
        if tile == 'X':
            return p


def build_map(m, dirs):
    cur = find_current_location(m)
    for d in dirs:
        # Build the walls
        for p in neighbours_diagonal(cur):
            if p in m:
                if m[p] != '#':
                    raise Exception('diagonals should be walls {p}: {m[p]}')
            m[p] = '#'
        
        # Move to new room
        if d == 'E':
            m[cur] = '.'
            m[east(cur)] = '|'
            cur = east(east(cur))
            m[cur] = 'X'
        if d == 'N':
            m[cur] = '.'
            m[north(cur)] = '-'
            cur = north(north(cur))
            m[cur] = 'X'
        if d == 'W':
            m[cur] = '.'
            m[west(cur)] = '|'
            cur = west(west(cur))
            m[cur] = 'X'
        if d == 'S':
            m[cur] = '.'
            m[south(cur)] = '-'
            cur = south(south(cur))
            m[cur] = 'X'

    fill_unknowns_with_walls(m)
    return m


def find_matching_paren(re, i):
    parens = 0
    while i < len(re):
        if re[i] == '(':
            parens += 1
        if re[i] == ')':
            parens -= 1
            if parens == 0:
                print(i)
        i += 1

    return -1

def parse_regex(re):
    paths = []

    def parse(i, re, path):
        print(i, re)
        parens = 0
        while re[i] != '$':
            if c == '^':
                i += 1
            if c == '$':
                paths.append(path)
                return
            if c in 'NSEW':
                path.append(c)
                i += 1
            if re[i] == '|':
                if parens == 1:
                    pipe_idx = j
            if c == '(':
                p = find_matching_paren(re, i)
                if p == -1:
                    raise Exception(f'Paren match error: index out of bounds parens {parens} len(re) {len(re)}, i {i}')






def main():
    assert(find_matching_paren('^N(E|W)N$', 2) == 6)
    assert(find_matching_paren('^ENWWW(NEEE|SSE(EE|N))$', 6) == 21)
    assert(find_matching_paren('^ENWWW(NEEE|SSE(EE|N))$', 15) == 20)
    # parse_regex('^WNE$^ENWWW(NEEE|SSE(EE|N))$')


if __name__ == '__main__':
    main()
