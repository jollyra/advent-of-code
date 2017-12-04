#! /usr/bin/env python3

import sys


def main():
    with open(sys.argv[1], 'r') as fh:
        valid_count = 0
        for line in fh:
            valid = True
            cache = set()
            words = line.strip().split()
            for w in words:
                if w in cache:
                    valid = False
                    break
                else:
                    cache.add(w)
            if valid:
                valid_count += 1
        print(valid_count)


if __name__ == '__main__':
    main()
