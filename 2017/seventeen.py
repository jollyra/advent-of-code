#! /usr/bin/env python3


def generate_seq(step, end):
    seq = []
    cur = 0
    for i in range(1, 2019):
        cur = (cur + step) % i + 1
        seq.insert(cur, i)
    return seq


def vortex_index(target_index, step, rounds):
    cur = 0
    num = 0
    for i in range(1, rounds + 2):
        cur = (cur + step) % i + 1
        if cur == target_index:
            num = i
    return num


if __name__ == '__main__':
    seq = generate_seq(371, 2017)
    part1 = seq[seq.index(2017) + 1]
    print(f'part 1: {part1}')

    part2 = vortex_index(1, 371, int(5e7))
    print(f'part 2: {part2}')
