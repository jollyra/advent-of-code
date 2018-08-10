#!/usr/bin/env python3


import sys


def init_grid(size):
    grid = []
    for i in range(size):
        grid.append([0 for _ in range(size)])
    return grid


def parse_arg(arg):
    p = arg.split(',')
    return (int(p[0].strip()), int(p[1].strip()))


def input_lines(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.split('-')
            command = line[0].strip()
            args = line[1].split('through')
            instructions.append((command, parse_arg(args[0]), parse_arg(args[1])))
    return instructions


def write_rect(grid, topleft, botright, mutation_func):
    x0, y0 = topleft
    x1, y1 = botright
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            grid[y][x] = mutation_func(grid[y][x])


def execute(grid, instruction, version=0):
    cmd, arg0, arg1 = instruction
    if cmd == 'turn on':
        if version == 0:
            write_rect(grid, arg0, arg1, lambda x: 1)
        elif version == 1:
            write_rect(grid, arg0, arg1, lambda x: x + 1)
    elif cmd == 'toggle':
        if version == 0:
            write_rect(grid, arg0, arg1, lambda x: x ^ 1)
        elif version == 1:
            write_rect(grid, arg0, arg1, lambda x: x + 2)
    elif cmd == 'turn off':
        if version == 0:
            write_rect(grid, arg0, arg1, lambda x: 0)
        elif version == 1:
            write_rect(grid, arg0, arg1, lambda x: x - 1 if x != 0 else 0)
    else:
        print('unrecognized commmand', cmd)


def count_brightness(grid):
    count = 0
    for y in grid:
        for x in y:
            count += x
    return count


if __name__ == '__main__':
    instructions = input_lines(sys.argv[1])
    grid_size = int(sys.argv[2])
    version = int(sys.argv[3])
    grid = init_grid(grid_size)
    for ins in instructions:
        execute(grid, ins, version=version)
    print('total brightness is {}'.format(count_brightness(grid)))
