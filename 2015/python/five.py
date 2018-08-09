#!/usr/bin/env python3


import sys


def contains_three_vowels(s):
    vowels = 'aeiou'
    count = 0
    for c in s:
        if c in vowels:
            count += 1
    return count >= 3


def contains_double_letter(s):
    i = 0
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            return True
        i += 1
    return False


def contains_strings(test_string, search_strings):
    for s in search_strings:
        if s in test_string:
            return True
    return False


def cond_a(s):
    i = 0
    while i < len(s) - 1:
        pair = s[i:i+2]
        if pair in s[:i] or pair in s[i+2:]:
            return True
        i += 1
    return False


def cond_b(s):
    i = 0
    while i < len(s) - 2:
        if s[i] == s[i + 2]:
            return True
        i += 1
    return False


def is_nice_string(s):
    return contains_three_vowels(s) and contains_double_letter(s) and not contains_strings(s, ['ab', 'cd', 'pq', 'xy'])


def is_nice_string_p2(s):
    return cond_a(s) and cond_b(s)


def input_line(filename):
    with open(filename, 'r') as f:
        return [l for l in f]


if __name__ == '__main__':
    assert is_nice_string('ugknbfddgicrmopn') is True
    assert is_nice_string('aaa') is True
    assert is_nice_string('jchzalrnumimnmhp') is False
    assert is_nice_string('haegwjzuvuyypxyu') is False
    assert is_nice_string('dvszwmarrgswjxmb') is False
    assert is_nice_string_p2('qjhvhtzxzqqjkmpb') is True
    assert is_nice_string_p2('xxyxx') is True
    assert is_nice_string_p2('uurcxstgmygtbstg') is False
    assert is_nice_string_p2('ieodomkazucvgmuy') is False
    print('pass')

    strings = input_line(sys.argv[1])
    nice_strings = [s for s in strings if is_nice_string(s)]
    print('ans: {}'.format(len(nice_strings)))

    nice_strings = [s for s in strings if is_nice_string_p2(s)]
    print('ans: {}'.format(len(nice_strings)))
