#! /usr/bin/env python3


def count_groups(lines):
    E = {l[0]: l[1:] for l in lines}
    V = set(E.keys())
    visited = set()
    count = 0
    while V > visited:
        unvisited = V - visited
        start = unvisited.pop()
        dfs(start, E, visited)
        count += 1
    return count


def dfs(current_v, E, visited):
    visited.add(current_v)
    horizon = [v for v in E[current_v] if v not in visited]
    for v in horizon:
        dfs(v, E, visited)


if __name__ == '__main__':
    with open('in.txt', 'r') as f:
        lines = [line.strip().split() for line in f]
        print('# of groups is', count_groups(lines))
