#! /usr/bin/env python3


from collections import namedtuple


Cube = namedtuple('CubeCoordinate', 'x, y, z')


def fewest_steps(path):
    path = path.split(',')
    origin = Cube(x=0, y=0, z=0)
    dest = get_cube_coord_from_path(path)
    return dist(dest, origin)


def furthest_away(path):
    path = path.split(',')
    max_dist = 0
    for i in range(1, len(path)):
        subpath = path[:i]
        dest = get_cube_coord_from_path(subpath)
        subpath_dist = dist(dest, Cube(x=0, y=0, z=0))
        if subpath_dist > max_dist:
            max_dist = subpath_dist
    return max_dist


def get_cube_coord_from_path(path):
    directions = {'ne': 0, 'se': 0, 's': 0, 'sw': 0, 'nw': 0, 'n': 0}
    for d in path:
        directions[d] += 1

    x = directions['ne'] + directions['se'] - directions['nw'] - directions['sw']
    y = directions['sw'] + directions['s'] - directions['ne'] - directions['n']
    z = directions['nw'] + directions['n'] - directions['se'] - directions['s']
    cube = Cube(x=x, y=y, z=z)
    return cube


def dist(a, b):
    return max(abs(a.x - b.x), abs(a.y - b.y), abs(a.z - b.z))


def Input():
    with open('11_input.txt', 'r') as f:
        line = f.read()
        return line.strip()


if __name__ == '__main__':
    assert(fewest_steps('ne,ne,ne') == 3)
    assert(fewest_steps('ne,ne,sw,sw') == 0)
    assert(fewest_steps('ne,ne,s,s') == 2)
    assert(fewest_steps('se,sw,se,sw,sw') == 3)
    assert(fewest_steps('ne,ne,se') == 3)
    print('pass')

    assert(furthest_away('ne,ne,s,s') == 2)
    print('pass')

    path = Input()
    print('fewest steps:', fewest_steps(path))
    print('furthest away:', furthest_away(path))
