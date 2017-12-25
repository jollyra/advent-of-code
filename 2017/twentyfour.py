#! /usr/bin/env python3


def max_strength(G, node):
    horizon = []
    for v in G:
        if node[1] == v[0]:
            horizon.append(v)
        elif node[1] == v[1]:
            horizon.append(v[::-1])

    if not horizon:
        return node[1]

    return max([node[1] + v[0] + max_strength(difference(G, v), v) for v in horizon])


def max_depth(G, node, path):
    horizon = []
    for v in G:
        if node[1] == v[0]:
            horizon.append(v)
        elif node[1] == v[1]:
            horizon.append(v[::-1])

    if not horizon:
        if len(path) > 30:
        # if len(path) >= 4:
            print('len of path', len(path))
            acc = 0
            for p in path:
                acc += p[0] + p[1]
            print('acc', acc)
        return 0

    return max(1, *[1 + max_depth(difference(G, v), v, path + [v]) for v in horizon])


def seen(v, path):
    return v in path or v[::-1] in path


def difference(s, el):
    return s - {el, el[::-1]}


def Input():
    with open('24_input.txt', 'r') as f:
        return [tuple(line.strip().split('/')) for line in f]


if __name__ == '__main__':
    test_graph = {(0, 2), (2, 2), (2, 3), (3, 4), (3, 5), (0, 1), (10, 1), (9, 10)}
    assert(max_strength(test_graph, (0, 0)) == 31)
    print(max_depth(test_graph, (0, 0), []))
    # assert(max_depth(test_graph, (0, 0), []) == 19)

    seq = Input()
    G = {(int(x[0]), int(x[1])) for x in seq}
    # part1 = max_strength(G, (0, 0))
    # print('part1', part1)
    
    part2 = max_depth(G, (0, 0), [])
    print('part2', part2)
