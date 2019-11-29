from util import *
from collections import deque


def new_grid(filename):
    grid = []
    for line in inputs(filename):
        row = []
        for tile in line:
            if tile in 'E':
                row.append((tile, 3, 200, 'G'))
            elif tile in 'G':
                row.append((tile, 3, 200, 'E'))
            else:
                row.append((tile))
        grid.append(row)
    return grid


def render_grid(grid):
    for row in grid:
        for x in row:
            print(x[0], end='')
        print()


def reading_order_neighbours4(point):
    x, y = point
    return [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]


def in_bounds(grid, point):
    return 0 <= X(point) < len(grid[0]) and 0 <= Y(point) < len(grid)


def get(grid, p):
    return grid[Y(p)][X(p)]

def set(grid, p, val):
    x, y = p
    grid[y][x] = val


def get_path(paths, p):
    path = []
    while paths[p]:
        path.append(p)
        p = paths[p]
    path.append(p)
    path.reverse()
    return path


def reading_order_bfs(grid, src, target):
    horizon = deque()
    horizon.append(src)
    path = {src: None}
    while horizon:
        cur = horizon.popleft()
        # print(cur)
        # print(horizon)
        # print(path)
        for n in reading_order_neighbours4(cur):
            if in_bounds(grid, n):  # TODO move this logic out of here
                tile = get(grid, n)
                if tile[0] == '.' and n not in path:
                    horizon.append(n)
                    path[n] = cur
                if tile[0] == target:
                    path[n] = cur
                    return get_path(path, n)
    return []


def main():
    grid = new_grid('15_test.in')
    render_grid(grid)
    path = reading_order_bfs(grid, (1, 1), 'G')
    print('path:', path)

    attack_order = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            p = (x, y)
            tile = get(grid, p)
            if tile[0] in 'EG':
                attack_order.append(p)

    for p in attack_order:
        entity = get(grid, p)
        path = reading_order_bfs(grid, p, entity[3])
        if path:
            q = path[1]
            set(grid, p, '.')
            set(grid, q, entity)
            render_grid(grid)



if __name__ == '__main__':
    main()
