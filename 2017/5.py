#! /usr/bin/env python3


def jump_around(instructions):
    count = 0
    ip = 0
    while ip < len(instructions):
        cur = instructions[ip]
        if cur >= 3:
            instructions[ip] -= 1
        else:
            instructions[ip] += 1
        ip += cur
        count += 1
    return count


def Input():
    with open('in.txt', 'r') as f:
        instructions = [int(line.strip()) for line in f]
        return instructions


def main():
    assert jump_around([0, 3, 0, 1, -3]) == 10
    print(jump_around(Input()))


if __name__ == '__main__':
    main()
