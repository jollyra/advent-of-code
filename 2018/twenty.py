from functools import lru_cache


def neighbours_diagonal(point):
    """Only diagonals returned in order quadrants I, II, III, IV (CCW)."""
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


def X(point): return point[0]
def Y(point): return point[1]


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


def step(coords, cur, direction):
    # Build the walls
    for p in neighbours_diagonal(cur):
        if p in coords:
            if coords[p] != '#':
                raise Exception('diagonals should be walls {p}: {coords[p]}')
        coords[p] = '#'

    directions = {
        'E': (east,  '|'),
        'N': (north, '-'),
        'W': (west,  '|'), 
        'S': (south, '-'),
    }

    # Move to new room
    step_fn, door_type = directions[direction]
    coords[step_fn(cur)] = door_type
    cur = step_fn(step_fn(cur))
    coords[cur] = '.'

    return cur


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


class Node:
    count = 0

    def __init__(self):
        self.v = ''
        self.N = []
        self.id = self._get_id()

    def _get_id(self):
        Node.count += 1
        return Node.count

    def add_value(self, value):
        self.v += value

    def add_child(self, node):
        self.N.append(node)

    def __str__(self):
        return f'node {self.id} value {self.v} children {[node for node in self.N]}'

    def __repr__(self):
        return f'{self.id}'

    def size(self):
        print(self.id)
        return 1 + sum(n.size() for n in self.N)


def shortest_path_to_farthest_door(re):
    src = (0, 0)
    node = parse_regex(re)
    print('calculating size of tree...')
    print(f'regex parsed. size of tree is {node.size()}')
    # print_preorder_traversal(node)
    coords = build_map(node)
    costs = bfs(coords, src)
    return max(costs.values())


def print_preorder_traversal(node):
    print(node)
    for n in node.N:
        print_preorder_traversal(n)


def build_map(node):
    print('build_map')
    cur = (0, 0)
    coords = {cur: 'X'}

    # TODO: this is probably getting caught in cycles like node.size()
    def preorder_traversal(node, current_point):
        for direction in node.v:
            current_point = step(coords, current_point, direction)
        for n in node.N:
            preorder_traversal(n, current_point)

    preorder_traversal(node, cur)
    fill_unknowns_with_walls(coords)
    return coords


@lru_cache(maxsize=None)
def parse_regex(re):
    i = 0
    node = Node()
    while i < len(re):
        if re[i] == '^':
            i += 1
        if re[i] == '$':
            print(parse_regex.cache_info())
            return node
        if re[i] in 'NSEW':
            node.add_value(re[i])
            i += 1
        if re[i] == '(':
            open_paren_idx = i
            close_paren_idx, pipe_idxs = find_matching_paren(re, open_paren_idx)
            if close_paren_idx == -1:
                raise Exception(f'Paren match error: no matching close paren found')

            rest_of_re = re[close_paren_idx+1:]
            if len(pipe_idxs) == 0:
                raise Exception(f'Paren match error: no pipes found')
            else:
                p = open_paren_idx
                q = 0
                while q < len(pipe_idxs):
                    branch = re[p+1:pipe_idxs[q]]
                    node.add_child(parse_regex(branch + rest_of_re))
                    p = pipe_idxs[q]  # Move past the pipe we just used
                    q += 1

                branch = re[pipe_idxs[-1]+1:close_paren_idx]
                node.add_child(parse_regex(branch + rest_of_re))
            return node

    return node


def bfs(coords, src):
    print('bfs')
    horizon = [src]
    costs = {src: 0}
    while horizon:
        cur = horizon.pop(-1)
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
    assert(test_shortest_path('^WNE$', 3))
    assert(test_shortest_path('^ENWWW(NEEE|SSE(EE|N))$', 10))
    assert(test_shortest_path('^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$', 18))
    assert(test_shortest_path('^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$', 23))
    assert(test_shortest_path('^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$', 31))
    print('pass')

    # with open('20_input.txt', 'r') as f:
    #     re = f.read().strip()
    #     print('\npart 1')
    #     print(shortest_path_to_farthest_door(re))


if __name__ == '__main__':
    main()
