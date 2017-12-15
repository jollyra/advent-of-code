#! /usr/bin/env python3


import sys


def judge(rounds, generator_a, generator_b, compare_func):
    matches = 0
    for a, b in zip(generator_a, generator_b):
        if compare_func(a, b):
            matches += 1
        rounds -= 1
        if rounds == 0:
            return matches


def generator_part1(seed, factor):
    x = (seed * factor) % 2147483647
    while True:
        yield x
        x = (x * factor) % 2147483647


def generator_part2(seed, factor, mod_func):
    x = (seed * factor) % 2147483647
    while True:
        if mod_func(x):
            yield x
        x = (x * factor) % 2147483647


def compare_lower_16_bits(a, b):
    bitmask = 0b00000000000000001111111111111111
    a = a & bitmask
    b = b & bitmask
    return not (a ^ b)


def stardard_mod_4(x):
    return x % 4 == 0


def stardard_mod_8(x):
    return x % 8 == 0


def fast_mod_4(x):
    last2digits = int(str(x)[-2:])
    return True if last2digits % 4 else False


def fast_mod_8(x):
    last2digits = int(str(x)[-3:])
    return True if last2digits % 8 else False


if __name__ == '__main__':
    if sys.argv[1] == 'part1' or sys.argv[1] == 'both':
        generator_a = generator_part1(116, 16807)
        generator_b = generator_part1(299, 48271)
        part1_count = judge(int(4e7), generator_a, generator_b, compare_lower_16_bits)
        assert(part1_count == 569)
        print('part 1:', part1_count)

    elif sys.argv[1] == 'part2' or sys.argv[1] == 'both':
        generator_a = generator_part2(116, 16807, fast_mod_4)
        generator_b = generator_part2(299, 48271, fast_mod_8)
        part2_count = judge(int(5e6), generator_a, generator_b, compare_lower_16_bits)
        assert(part2_count == 298)
        print('part 2:', part2_count)
