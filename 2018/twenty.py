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
    for y in range(y_max, y_min - 1, -1):
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
    cur = (0, 0)
    for d in dirs:
        # Build the walls
        for p in neighbours_diagonal(cur):
            if p in m:
                if m[p] != '#':
                    raise Exception('diagonals should be walls {p}: {m[p]}')
            m[p] = '#'

        # Move to new room
        if d == 'E':
            m[east(cur)] = '|'
            cur = east(east(cur))
            m[cur] = '.'
        if d == 'N':
            m[north(cur)] = '-'
            cur = north(north(cur))
            m[cur] = '.'
        if d == 'W':
            m[west(cur)] = '|'
            cur = west(west(cur))
            m[cur] = '.'
        if d == 'S':
            m[south(cur)] = '-'
            cur = south(south(cur))
            m[cur] = '.'

    return m


def find_matching_paren(re, i):
    parens = 0
    pipe_idxs = []
    while i < len(re):
        if re[i] == '(':
            parens += 1
        if re[i] == ')':
            parens -= 1
            if parens == 0:
                return i, pipe_idxs
        if re[i] == '|' and parens == 1:
            pipe_idxs.append(i)
        i += 1

    return -1, []


def parse_regex(re):
    paths = []

    def parse(re, path):
        # print(re)
        i = 0
        while i < len(re):
            # print(i, re[i], path, paths)
            if re[i] == '^':
                i += 1
            if re[i] == '$':
                paths.append(path)
                return
            if re[i] in 'NSEW':
                path += re[i]
                i += 1
            if re[i] == '(':
                open_paren_idx = i
                close_paren_idx, pipe_idxs = find_matching_paren(re, open_paren_idx)
                if close_paren_idx == -1:
                    raise Exception(f'Paren match error: no matching close paren found')

                rest_of_re = re[close_paren_idx+1:]
                if len(pipe_idxs) == 0:
                    raise Exception(f'Paren match error: no pipes found')
                elif len(pipe_idxs) == 1:
                    branch_1 = re[open_paren_idx+1:pipe_idxs[0]]
                    branch_2 = re[pipe_idxs[0]+1:close_paren_idx]
                    parse(branch_1 + rest_of_re, path)
                    parse(branch_2 + rest_of_re, path)
                else:
                    p = open_paren_idx
                    q = 0
                    while q < len(pipe_idxs):
                        branch = re[p+1:pipe_idxs[q]]
                        parse(branch + rest_of_re, path)
                        p = pipe_idxs[q]  # Move past the pipe we just used
                        q += 1

                    branch = re[pipe_idxs[-1]+1:close_paren_idx]
                    parse(branch + rest_of_re, path)

                return

    parse(re, '')
    return paths


def test_parse_regex(re, want):
    paths = parse_regex(re)
    if len(paths) != len(want):
        print(f'expected {want} got {paths}')
        return False
    if all(s in want for s in paths):
        return True
    print(f'expected {want} got {paths}')
    return False


def main():
    assert(find_matching_paren('^N(E|W)N$', 2) == (6, [4]))
    assert(find_matching_paren('^ENWWW(NEEE|SSE(EE|N))$', 6) == (21, [11]))
    assert(find_matching_paren('^ENWWW(NEEE|SSE(EE|N))$', 15) == (20, [18]))
    assert(find_matching_paren('^(NEWS|WNSE|)$', 1) == (12, [6, 11]))
    assert(test_parse_regex('^N(E|W)N$', ['NEN', 'NWN']))
    assert(test_parse_regex('^N(E|)N$', ['NEN', 'NN']))
    assert(test_parse_regex('^ENWWW(NEEE|SSE(EE|N))$', ['ENWWWNEEE', 'ENWWWSSEEE', 'ENWWWSSEN']))
    assert(test_parse_regex('^(NEWS|WNSE|NNNN)$', ['NEWS', 'WNSE', 'NNNN']))
    assert(test_parse_regex('^(NEWS|WNSE|)$', ['NEWS', 'WNSE', '']))
    print('pass')

    m = {(0, 0): 'X'}
    paths = parse_regex('^WNE$')
    for path in paths:
        m = build_map(m, path)
    fill_unknowns_with_walls(m)
    render_map(m)

    m = {(0, 0): 'X'}
    paths = parse_regex('^N(E|W)N$')
    for path in paths:
        m = build_map(m, path)
    fill_unknowns_with_walls(m)
    render_map(m)

    m = {(0, 0): 'X'}
    paths = parse_regex('^ENWWW(NEEE|SSE(EE|N))$')
    for path in paths:
        m = build_map(m, path)
    fill_unknowns_with_walls(m)
    render_map(m)


if __name__ == '__main__':
    main()
