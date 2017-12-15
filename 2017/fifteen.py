#! /usr/bin/env python3


def judge(rounds, generator_a, generator_b):
    matches = 0
    for a, b in zip(generator_a, generator_b):
        if compare_lower_16_bits(a, b):
            matches += 1
        rounds -= 1
        if rounds == 0:
            return matches


def generator_part1(seed, factor):
    x = (seed * factor) % 2147483647
    while 1:
        yield x
        x = (x * factor) % 2147483647


def generator_part2(seed, factor, denominator):
    x = (seed * factor) % 2147483647
    while 1:
        if x % denominator == 0:
            yield x
        x = (x * factor) % 2147483647


def compare_lower_16_bits(a, b):
    bitmask = 0b00000000000000001111111111111111
    a = a & bitmask
    b = b & bitmask
    return not (a ^ b)


if __name__ == '__main__':
    generator_a = generator_part1(116, 16807)
    generator_b = generator_part1(299, 48271)
    part1_count = judge(4*10**7, generator_a, generator_b)
    assert(part1_count == 569)
    print('part 1:', part1_count)

    generator_a = generator_part2(116, 16807, 4)
    generator_b = generator_part2(299, 48271, 8)
    part2_count = judge(5*10**6, generator_a, generator_b)
    assert(part2_count == 298)
    print('part 2:', part2_count)
