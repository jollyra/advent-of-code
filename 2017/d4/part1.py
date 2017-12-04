#! /usr/bin/env python3

from util import *
import sys


def main():
    with open(sys.argv[1], 'r') as fh:
        valid = 0
        invalid = 0
        for line in fh:
            good = True
            counter = Counter()
            line = line.strip()
            words = line.split()
            for word in words:
                counter[word] += 1
            for key, val in counter.items():
                if val > 1:
                    good = False
                    break
            if good:
                valid += 1
            else:
                invalid += 1
        print('valid: {} invalid: {}'.format(valid, invalid))




if __name__ == '__main__':
    main()
