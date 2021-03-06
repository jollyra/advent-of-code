#! /usr/bin/env python3

import re
from collections import namedtuple, Counter


Room = namedtuple('Room', ['name', 'sector', 'checksum'])
cat = ''.join
alphabet = 'abcdefghijklmnopqrstuvwxyz'


def main():
    assert isvalid(parse('aaaaa-bbb-z-y-x-123[abxyz]')) is True
    assert isvalid(parse('totally-real-room-200[decoy]')) is False
    assert ShiftCipher(alphabet).decrypt('qzmt-zixmtkozy-ivhz', 343) == 'very-encrypted-name'
    print('pass')

    rooms = [parse(line) for line in input()]
    valid_rooms = [room for room in rooms if isvalid(room)]
    ans = sum([room.sector for room in valid_rooms])
    print(f'part 1: {ans}')

    for room in valid_rooms:
        shift_cipher = ShiftCipher(alphabet)
        decrypted_name = shift_cipher.decrypt(room.name, room.sector)
        print(f'{decrypted_name}: {room}')


def isvalid(room):
    counter = Counter(room.name.replace('-', ''))
    counts = [(x[0], x[1]) for x in counter.items()]
    counts.sort(key=lambda t: t[0])
    counts.sort(key=lambda t: t[1], reverse=True)
    checksum = cat([t[0] for t in counts[:5]])
    return checksum == room.checksum


class ShiftCipher:
    def __init__(self, alphabet):
        self.alphabet = alphabet

    def decrypt(self, ciphertext, rotation):
        plaintext = list(ciphertext[:])
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
    with open('4_input.txt', 'r') as f:
        for line in f:
            yield line.strip()


if __name__ == '__main__':
    main()
