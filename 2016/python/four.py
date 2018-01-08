#! /usr/bin/env python3

import re
from collections import namedtuple, Counter


Room = namedtuple('Room', ['name', 'sector', 'checksum'])
cat = ''.join


def main():
    rooms = input()
    assert isvalid(parse('aaaaa-bbb-z-y-x-123[abxyz]')) is True
    assert isvalid(parse('totally-real-room-200[decoy]')) is False
    assert ShiftCipher('qzmt-zixmtkozy-ivhz').decrypt(343) == 'very-encrypted-name'
    print('pass')

    valid_rooms = [room for room in rooms if isvalid(room)]
    ans = sum([room.sector for room in valid_rooms])
    print(f'part 1: {ans}')

    for room in valid_rooms:
        shift_cipher = ShiftCipher(room.name)
        decrypted_name = shift_cipher.decrypt(room.sector)
        print(f'{decrypted_name}: {room}')


def isvalid(room):
    counter = Counter(room.name.replace('-', ''))
    counts = [(x[0], x[1]) for x in counter.items()]
    counts.sort(key=lambda t: t[0])
    counts.sort(key=lambda t: t[1], reverse=True)
    checksum = cat([t[0] for t in counts[:5]])
    return checksum == room.checksum


class ShiftCipher:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self, ciphertext):
        self.ciphertext = list(ciphertext)

    def decrypt(self, rotation):
        plaintext = self.ciphertext[:]
        for cur, char in enumerate(plaintext):
            if char not in self.alphabet:
                continue
            idx = self.alphabet.index(char)
            idx_rot = (idx + rotation) % len(self.alphabet)
            plaintext[cur] = self.alphabet[idx_rot]
        return ''.join(plaintext)


def parse(line):
    match = re.match(r'^(.*)-(\d+)\[(.*)\]$', line)
    if match:
        name, sector, checksum = match.groups()
        return Room(name, int(sector), checksum)
    else:
        raise ValueError(f'malformed line {line}')


def input():
    with open('2_input.txt', 'r') as f:
        return [parse(line.strip()) for line in f]


if __name__ == '__main__':
    main()
