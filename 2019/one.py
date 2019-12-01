#!/usr/bin/env python3

from itertools import combinations, permutations
from collections import deque, Counter, defaultdict
from util import *


def main():
    lines = inputs('1_test.in')
    ts = []
    for line in lines:
        t = int(line)
        while True:
            t = (t // 3) - 2
            if t > 0:
                ts.append(t)
            else:
                break
    print(sum(ts))


if __name__ == '__main__':
    main()
