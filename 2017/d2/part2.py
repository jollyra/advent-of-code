#!/usr/bin/env python3

import sys


def main():
    str = sys.stdin.read()
    lines = str.split('\n')
    sum = 0
    for line in lines:
        nums = line.strip().split()
        nums = list(map(int, nums))
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j and x % y == 0:
                    sum += x/y
    print(sum)


if __name__ == '__main__':
    main()
