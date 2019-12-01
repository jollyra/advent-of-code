#!/usr/bin/env python3

with open('1.in', 'r') as f:
    acc = 0
    for line in f:
        x = int(line)
        while True:
            x = x // 3 - 2
            if x > 0:
                acc += x
            else:
                break
    print('Part 2:', acc)
