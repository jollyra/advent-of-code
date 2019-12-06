#!/usr/bin/env python3
from collections import defaultdict


def djikstras(E, src):
    costs = {src: 0}
    horizon = [src]
    while horizon:
        cur = horizon.pop(-1)
        for v in [v for v in E[cur]]:
            cur_cost = costs[cur] + 1
            if v in costs and costs[v] < cur_cost:
                continue
            horizon.append(v)
            costs[v] = cur_cost
    return costs


def input_E(filename):
    E = defaultdict(list)
    with open(filename, 'r') as f:
        for line in f:
            v1, v2 = line.strip().split(')')
            E[v1].append(v2)
            E[v2].append(v1)
    return E


def main():
    E = input_E('6.in')
    costs = djikstras(E, 'YOU')

    acc = sum(c for c in costs.values())
    print(f'Part 1 total no. of direct and indirect orbits {acc}')

    cost = costs['SAN'] - 2
    print(f'Part 2 orbinal transfers from YOU -> SAN {cost}')


if __name__ == '__main__':
    main()
