#!/usr/bin/env python3


def main():
    target = int(input().strip())
    val = traverse(target)
    print('ans: {}'.format(val))


def traverse(target):
    # COO (x, y, val)
    coordinate_list = [(0, 0, 1)]  # seed
    layer = 1
    while True:
        x, y = get_start_xy(layer)
        cells = cells_in_layer(layer)
        segment_size = cells // 4

        # up
        for i in range(segment_size - 1):
            val = write(coordinate_list, (x, y))
            if val > target:
                return val
            # print('(x, y) {},{}'.format(x, y))
            y += 1

        # left
        for i in range(segment_size):
            val = write(coordinate_list, (x, y))
            if val > target:
                return val
            # print('(x, y) {},{}'.format(x, y))
            x -= 1

        # down
        for i in range(segment_size):
            val = write(coordinate_list, (x, y))
            if val > target:
                return val
            # print('(x, y) {},{}'.format(x, y))
            y -= 1

        # right
        for i in range(segment_size + 1):
            val = write(coordinate_list, (x, y))
            if val > target:
                return val
            # print('(x, y) {},{}'.format(x, y))
            x += 1

        layer += 1


def get_start_xy(layer):
    return 1 * layer, -1 * (layer - 1)


def cells_in_layer(layer):
    if layer == 0:
        return 1
    else:
        return 8 * layer


def write(coordinate_list, cell):
    adjacents = find_adjacent(cell)
    x, y = cell
    val = sum_cells(coordinate_list, adjacents)
    coordinate_list.append((x, y, val))
    return val


def sum_cells(coordinate_list, adjacents):
    acc = 0
    for coord in adjacents:
        cell = get_coord(coordinate_list, coord)
        if cell:
            x, y, val = cell
            acc += val
    return acc


def get_coord(coordinate_list, coord):
    for c in coordinate_list:
        x, y, val = c
        if (x, y) == coord:
            return c
    return None


def find_adjacent(cell):
    x, y = cell
    return [(x + i, y + j) for i in [-1, 0, 1] for j in [-1, 0, 1] if not i == j == 0]


if __name__ == '__main__':
    main()
