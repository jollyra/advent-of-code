from util import *
from collections import deque


def new_grid(filename):
    return inputs(filename)


def render_grid(grid):
    for row in grid:
        print(row)


def reading_order_neighbours4(point):
    x, y = point
    return [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]


def in_bounds(grid, point):
    return 0 <= X(point) < len(grid[0]) and 0 <= Y(point) < len(grid)


def get(grid, p):
    return grid[Y(p)][X(p)]


def reading_order_bfs(grid, src, target):
    horizon = deque()
    horizon.append(src)
    path = {src: None}
    while horizon:
        cur = horizon.popleft()
        print(cur)
        print(horizon)
        print(path)
        for n in reading_order_neighbours4(cur):
            if in_bounds(grid, n):  # TODO move this logic out of here
                tile = get(grid, n)
                if tile == '.' and n not in path:
                    horizon.append(n)
                    path[n] = cur
                if tile == target:
                    path[n] = cur
                    print('path', path)
                    return path
    return None


def main():
    grid = new_grid('15_test.in')
    render_grid(grid)
    path = reading_order_bfs(grid, (1, 1), 'G')
    print(path)


if __name__ == '__main__':
    main()
