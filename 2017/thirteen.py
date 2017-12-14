#! /usr/bin/env python3


from util import *
from functools import lru_cache
from copy import deepcopy



def do_work(seqs):
    layers = build_layers(seqs)
    scanners = [[0, 'd']] * len(layers)
    for delay in range(10**7):
        if delay % 10000 == 0:
            print(delay)
        scanners_copy = deepcopy(scanners)
        cost = calculate_cost(scanners_copy, layers)
        if cost is False:
            return delay
        scanners = update_scanners(layers, scanners)


def calculate_cost(scanners, layers):
    packet = 0
    # cost = 0
    while packet < len(layers):
        caught = check_collisions(packet, scanners, layers)
        if caught:
            return True
            # cost += packet * layers[packet]
        scanners = update_scanners(layers, scanners)
        packet += 1
    return False


def build_layers(seqs):
    m = max(seqs, key=lambda x: x[0])[0]
    layers = [0] * (m + 1)
    for seq in seqs:
        d, r = seq
        layers[d] = r
    return layers


def check_collisions(packet, scanners, layers):
    if layers[packet] > 0:
        return scanners[packet][0] == 0
    else:
        return False


def update_scanners(layers, scanners):
    for i, s in enumerate(scanners):
        if layers[i] > 0:
            d, du = scanners[i]
            if du == 'd':
                d += 1
            else:
                d -= 1
            if d == 0:
                du = 'd'
            elif d == layers[i] - 1:
                du = 'u'
            scanners[i] = [d, du]
    return scanners


def input_seqs(sep=None):
    'Read multuple line-separated seqs from a file'
    seqs = []
    # with open('tst.txt', 'r') as f:
    with open('thirteen_input.txt', 'r') as f:
        for line in f:
            seqs.append([int(el) for el in line.strip().split()])
    return seqs


if __name__ == '__main__':
    seqs = input_seqs()
    print('ans', do_work(seqs))
