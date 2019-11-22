from collections import defaultdict


def neighbours_diagonal(point):
    'Only diagonals returned in order quadrants I, II, III, IV (CCW).'
    x, y = point
    return [(x + 1, y + 1), (x - 1, y + 1), (x - 1, y - 1), (x + 1, y - 1)]


def X(point): return point[0]
def Y(point): return point[1]


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


def bounds(coords):
    x_min = x_max = y_min = y_max = 0
    for p in coords:
        x_max = max(x_max, X(p))
        x_min = min(x_min, X(p))
        y_max = max(y_max, Y(p))
        y_min = min(y_min, Y(p))
    return x_min, x_max, y_min, y_max


def fill_unknowns_with_walls(coords):
    x_min, x_max, y_min, y_max = bounds(coords)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            p = (x, y)
            if p not in coords:
                coords[p] = '#'


def render_map(coords):
    x_min, x_max, y_min, y_max = bounds(coords)
    for y in range(y_max, y_min - 1, -1):
        for x in range(x_min, x_max + 1):
            p = (x, y)
            if p in coords:
                print(coords[p], end='')
            else:
                print('?', end='')
        print()


def find_current_location(coords):
    for p, tile in coords.items():
        if tile == 'X':
            return p


def build_map(coords, paths):
    print('build_map')
    for path in paths:
        cur = (0, 0)
        for d in path:
            # Build the walls
            for p in neighbours_diagonal(cur):
                if p in coords:
                    if coords[p] != '#':
                        raise Exception('diagonals should be walls {p}: {coords[p]}')
                coords[p] = '#'

            # Move to new room
            if d == 'E':
                coords[east(cur)] = '|'
                cur = east(east(cur))
                coords[cur] = '.'
            if d == 'N':
                coords[north(cur)] = '-'
                cur = north(north(cur))
                coords[cur] = '.'
            if d == 'W':
                coords[west(cur)] = '|'
                cur = west(west(cur))
                coords[cur] = '.'
            if d == 'S':
                coords[south(cur)] = '-'
                cur = south(south(cur))
                coords[cur] = '.'

    fill_unknowns_with_walls(coords)
    return coords


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
    print('parse_regex')
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


def neighbours4(point):
    x, y = point
    return [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]


def bfs(coords, src):
    print('bfs')
    horizon = [src]
    costs = {src: 0}
    while horizon:
        # print(len(horizon))
        # print(f'horizon {horizon}')
        # print(f'costs {costs}')
        cur = horizon.pop(-1)
        # print(cur)
        for step_fn in [east, north, west, south]:
            if coords[step_fn(cur)] in '|-':
                nxt = step_fn(step_fn(cur))
                if nxt in costs:
                    if costs[nxt] > costs[cur] + 1:
                        horizon.append(nxt)
                else:
                    costs[nxt] = costs[cur] + 1
                    horizon.append(nxt)

    return costs


def shortest_path_to_farthest_door(re):
    src = (0, 0)
    coords = {src: 'X'}
    paths = parse_regex(re)
    coords = build_map(coords, paths)
    costs = bfs(coords, src)
    return max(costs.values())


def test_parse_regex(re, want):
    paths = parse_regex(re)
    if len(paths) != len(want):
        print(f'expected {want} got {paths}')
        return False
    if all(s in want for s in paths):
        return True
    print(f'expected {want} got {paths}')
    return False


def test_shortest_path(re, want):
    got = shortest_path_to_farthest_door(re)
    if got == want:
        return True
    print(f'expected {want} got {cost}')
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
    assert(test_shortest_path('^ENWWW(NEEE|SSE(EE|N))$', 10))
    assert(test_shortest_path('^WNE$', 3))
    assert(test_shortest_path('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$', 18))
    assert(test_shortest_path('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$', 23))
    assert(test_shortest_path('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$', 31))
    print('pass')

    with open('20_input.txt', 'r') as f:
        re = f.read().strip()
        print('\npart 1')
        print(shortest_path_to_farthest_door(re))


if __name__ == '__main__':
    main()
