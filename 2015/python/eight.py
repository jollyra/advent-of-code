#!/usr/bin/env python3


def input_lines(filename):
    with open(filename, 'r') as f:
        return [line for line in f]
        # return [r'', r'abc', r'aaa\"aaa', r'\x27']


def len_in_memory(string):
    chars_in_memory = 0
    i = 0
    while i < len(string):
        slice = string[i:i + 2]
        if slice == '\\\\':
            i += 2
        elif slice == '\\x':
            i += 4
        elif slice == '\\"':
            i += 2
        else:
            i += 1
        chars_in_memory += 1

    return chars_in_memory


def len_in_code(string):
    return len(string) + 2


def len_encoded(string):
    len_encoded = 0
    for c in string:
        if c == '\"' or c == '\\':
            len_encoded += 2
        else:
            len_encoded += 1
    return len_encoded + 4


if __name__ == '__main__':
    assert len_in_memory(r'') == 0
    assert len_in_memory(r'abc') == 3
    assert len_in_memory(r'aaa\"aaa') == 7
    assert len_in_memory(r'\x27') == 1
    assert len_in_memory(r'\\') == 1
    print('pass')
    
    strings = input_lines('8.in')
    chars_in_mem = sum(len_in_memory(s) for s in strings)
    chars_in_code = sum(len_in_code(s) for s in strings)
    chars_in_encoded = sum(len_encoded(s) for s in strings)
    print('part 1:', chars_in_code - chars_in_mem)
    print('part 2:', chars_in_encoded - chars_in_code)
