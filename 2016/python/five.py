#! /usr/bin/env python3


import hashlib
import re


def decode_a(ciphertext):
    plaintext = ''
    generator = next_char_generator_a(ciphertext)
    for _ in range(8):
        plaintext += next(generator)
    return plaintext


def next_char_generator_a(ciphertext):
    count = 0
    while True:
        string = '{}{}'.format(ciphertext, count)
        hashed_string = hashlib.md5(string.encode('utf-8')).hexdigest()
        if re.match(r'[0]{5}', hashed_string):
            yield hashed_string[5]
        count += 1


def decode_b(ciphertext):
    chars = [None] * 8
    generator = next_char_generator_b(ciphertext)
    for _ in range(8):
        pos, val = next(generator)
        chars[pos] = val
    return ''.join(chars)


def next_char_generator_b(ciphertext):
    seen = set()
    count = 0
    while True:
        string = '{}{}'.format(ciphertext, count)
        hashed_string = hashlib.md5(string.encode('utf-8')).hexdigest()
        if re.match(r'[0]{5}', hashed_string):
            try:
                pos = int(hashed_string[5])
            except ValueError:
                continue
            finally:
                count += 1
            if 0 <= pos < 8:
                val = hashed_string[6]
                if pos not in seen:
                    seen.add(pos)
                    yield (pos, val)
        count += 1


if __name__ == '__main__':
    assert decode_a('abc') == '18f47a30'
    assert decode_b('abc') == '05ace8e3'
    print('pass')
    print(decode_b('uqwqemis'))
