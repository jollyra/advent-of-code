#! /usr/bin/env python3


import sys
from collections import Counter


class Node:
    def __init__(self, n, w, c):
        self.name = n
        self.weight = w
        self.children = c


def find_imba(node):
    if len(node.children) == 0:
        return node.weight
    else:
        sub_weights = [find_imba(child) for child in node.children]
        if not all_equal(sub_weights):
            counter = Counter(sub_weights)
            misfit_val = min(counter, key=counter.get)
            common_val = max(counter, key=counter.get)
            misfit_idx = sub_weights.index(misfit_val)
            imba_node = node.children[misfit_idx]
            corrected_weight = imba_node.weight + common_val - misfit_val
            print('Node {} should weigh {}, not {}'.format(imba_node.name, corrected_weight, imba_node.weight))
        return node.weight + sum(sub_weights)


def all_equal(seq):
    return all([seq[0] == rest for rest in seq[1:]])


def parse_tree():
    adj_dict = dict()
    with open(sys.argv[1], 'r') as f:
        for line in f:
            line = line.strip().split()
            adj_dict[line[0]] = {'w': int(line[1]), 'c': line[2:]}
    return adj_dict


def build_tree(node_name, adj_dict):
    node = adj_dict[node_name]
    return Node(node_name, node['w'], [build_tree(child, adj_dict) for child in node['c']])


def find_root(adj_dict):
    lefts = set()
    rights = set()
    for k, v in adj_dict.items():
        lefts.add(k)
        for child in v['c']:
            rights.add(child)
    return (lefts - rights).pop()


if __name__ == '__main__':
    adj_dict = parse_tree()
    root_name = find_root(adj_dict)
    print('Root node is', root_name)
    tree = build_tree(root_name, adj_dict)
    find_imba(tree)
