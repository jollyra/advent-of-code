#!/usr/bin/env python3


from collections import defaultdict
import five as intcode
import doctest


def rot_left(v):
    '''
    >>> rot_left((0, 1))
    (-1, 0)
    >>> rot_left((-1, 0))
    (0, -1)
    >>> rot_left((0, -1))
    (1, 0)
    >>> rot_left((1, 0))
    (0, 1)
    '''
    return (-v[1], v[0])


def rot_right(v):
    '''
    >>> rot_right((0, 1))
    (1, 0)
    '''
    return (v[1], -v[0])


def add(p, q):
    '''
    >>> add((1, 2), (-1, -2))
    (0, 0)
    '''
    return (p[0] + q[0], p[1] + q[1])


def magnitude(p):
    return abs(p[0]) + abs(p[1])


def X(point): return point[0]
def Y(point): return point[1]
def bounds(coords):
    x_min = x_max = y_min = y_max = 0
    for p in coords:
        x_max = max(x_max, X(p))
        x_min = min(x_min, X(p))
        y_max = max(y_max, Y(p))
        y_min = min(y_min, Y(p))
    return x_min, x_max, y_min, y_max


def render_map(coords):
    x_min, x_max, y_min, y_max = bounds(coords)
    for y in range(y_max, y_min - 1, -1):
        for x in range(x_min, x_max + 1):
            p = (x, y)
            if p in coords:
                colour = coords[p]
                tile = '#' if colour == 1 else ' '
                print(tile, end='')
            else:
                print(' ', end='')
        print()


def main():
    black = 0
    white = 1
    left = 0
    right = 1
    
    prog = intcode.input_ints('11.in')
    coords = defaultdict(int)
    heading = (0, 1)
    cur = (0, 0)

    machine = intcode.run(prog)
    r = next(machine)  # init
    assert(r == None)

    while True:
        # print(cur, heading)
        try:
            colour = coords[cur]
            assert(colour in [0, 1])
            machine.send(colour)

            colour = next(machine)
            assert(colour in [0, 1])
            coords[cur] = colour

            turn = next(machine)
            assert(turn in [0, 1])
            if turn == left:
                heading = rot_left(heading)
            elif turn == right:
                heading = rot_right(heading)
            else:
                print('bad turn', turn)
                return
            assert(magnitude(heading) == 1)
            cur = add(cur, heading)
        except StopIteration as e:
            print('stopping iteration', e)
            break
    print(f'Part 1: {len(coords)} panels painted at least once')
    for k, v in coords.items():
        print(k, v)
    render_map(coords)



if __name__ == '__main__':
    doctest.testmod()
    main()
