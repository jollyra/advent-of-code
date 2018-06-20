#!/usr/bin/env python3


import re


def decompressed_len(s, version=1):
    partitioner_re = re.compile('([A-Z]+)?(\(\d+x\d+\))?(.*)')
    marker_re = re.compile('\((\d+)x(\d+)\)')
    rest = s
    count = 0
    while rest:
        head, marker, rest = partitioner_re.match(rest).groups()
        if head:
            count += len(head)
        if marker:
            num_chars, repeats = marker_re.match(marker).groups()
            num_chars, repeats = int(num_chars), int(repeats)
            if version == 1:
                count += len(rest[:num_chars] * repeats)
                rest = rest[num_chars:]
            elif version == 2:
                rest = rest[:num_chars] * repeats + rest[num_chars:]

    return count


def Input():
    with open('9_input.txt', 'r') as f:
        return f.read().strip()


if __name__ == '__main__':
    assert decompressed_len('ADVENT') == 6
    assert decompressed_len('A(1x5)BC') == 7
    assert decompressed_len('(3x3)XYZ') == 9
    assert decompressed_len('A(2x2)BCD(2x2)EFG') == 11
    assert decompressed_len('(6x1)(1x3)A') == 6
    assert decompressed_len('X(8x2)(3x3)ABCY') == 18
    assert decompressed_len('(3x3)XYZ', version=2) == 9
    assert decompressed_len('X(8x2)(3x3)ABCY', version=2) == 20
    assert decompressed_len('(27x12)(20x12)(13x14)(7x10)(1x12)A', version=2) == 241920
    assert decompressed_len('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', version=2) == 445
    print('pass')

    compressed_text = Input()
    print('part 1: {}'.format(decompressed_len(compressed_text)))
    print('part 2: {}'.format(decompressed_len(compressed_text, version=2)))
