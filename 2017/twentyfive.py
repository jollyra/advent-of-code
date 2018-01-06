#! /usr/bin/env python3


from collections import defaultdict


def execute():
    tape = defaultdict(int)
    state = 'A'
    cursor = 0
    for i in range(12208951):
        val = tape[cursor]
        if state == 'A':
            if val == 0:
                tape[cursor] = 1
                cursor += 1
                state = 'B'
            else:
                tape[cursor] = 0
                cursor -= 1
                state = 'E'

        elif state == 'B':
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = 'C'
            else:
                tape[cursor] = 0
                cursor += 1
                state = 'A'

        elif state == 'C':
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = 'D'
            else:
                tape[cursor] = 0
                cursor += 1
                state = 'C'

        elif state == 'D':
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = 'E'
            else:
                tape[cursor] = 0
                cursor -= 1
                state = 'F'

        elif state == 'E':
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = 'A'
            else:
                tape[cursor] = 1
                cursor -= 1
                state = 'C'

        elif state == 'F':
            if val == 0:
                tape[cursor] = 1
                cursor -= 1
                state = 'E'
            else:
                tape[cursor] = 1
                cursor += 1
                state = 'A'
    return tape


def show_tape(tape):
    indexes = sorted(tape)
    for i in indexes:
        print(tape[i], end='')
    print()


def checksum(tape):
    count = 0
    for v in tape.values():
        if v == 1:
            count += 1
    return count


if __name__ == '__main__':
    tape = execute()
    print('ans: ', checksum(tape))
