#!/usr/bin/env python3


from itertools import groupby
cons = ''.join


def two_adjacent_digits_are_the_same(n):
    return any(len(list(g)) >= 2 for _, g in groupby(str(n)))


def exactly_two_adjacent_digits_are_the_same(n):
    return any(len(list(g)) == 2 for _, g in groupby(str(n)))


def non_decreasing(n):
    return cons((sorted(str(n)))) == cons(str(n))


if __name__ == '__main__':
    my_range = range(172851, 675869 + 1)
    part_one = sum(two_adjacent_digits_are_the_same(n) and non_decreasing(n) for n in my_range)
    part_two = sum(exactly_two_adjacent_digits_are_the_same(n) and non_decreasing(n) for n in my_range)
    print('Part 1:', part_one)
    print('Part 2:', part_two)
