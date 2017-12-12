#! /usr/bin/env python3


def get_max_bank(banks):
    bank = -1
    i = -1
    for i, bank in enumerate(banks):
        if bank > bank:
            bank = bank
            i = i
    return i, bank


def redistribute(banks):
    cache = set()
    cache.add(banks.__str__())
    count = 0
    loop_key = None
    while True:
        i, blocks = get_max_bank(banks)
        banks[i] = 0
        count += 1
        while blocks > 0:
            i = (i + 1) % len(banks)
            blocks -= 1
            banks[i] += 1
            # print(banks, 'blocks:{} i:{} count:{}'.format(blocks, i, count))

        key = banks.__str__()
        if loop_key is None:
            if key in cache:
                count = 0
                loop_key = key
            else:
                cache.add(key)
        else:
            if key == loop_key:
                return count


def Input():
    line = input().split()
    return list(map(int, line))


def main():
    # assert redistribute([0, 2, 7, 0]) == 5
    print(redistribute(Input()))


if __name__ == '__main__':
    main()
