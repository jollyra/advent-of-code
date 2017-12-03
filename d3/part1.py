#!/usr/bin/env python3


def main():
    x = int(input().strip())
    layer, start = get_layer_and_start(x)
    print('layer:{} start:{}'.format(layer, start))
    x0, y0 = get_start_xy(layer)
    print('start x:{} start y:{}'.format(x0, y0))
    xf, yf = traverse(x0, y0, start, layer, x)
    print('final x:{} final y:{}'.format(xf, yf))
    print('manhattan distance: {}'.format(manhattan_dist(xf, yf)))


def manhattan_dist(x, y):
    return abs(x) + abs(y)


def get_layer_and_start(x):
    corners = [1]
    while corners[-1] < x:
        next = corners[-1] + 8 * len(corners)
        corners.append(next)
    print('corners: {}'.format(corners))
    return len(corners) - 1, corners[-2] + 1


def get_start_xy(layer):
    return 1 * layer, -1 * (layer - 1)


def traverse(x, y, count, layer, target):
    cells = cells_in_layer(layer)
    segment_size = cells // 4

    # up
    for i in range(segment_size - 1):
        if count == target:
            return x, y
        y += 1
        count += 1

    # left
    for i in range(segment_size):
        if count == target:
            return x, y
        x -= 1
        count += 1

    # down
    for i in range(segment_size):
        if count == target:
            return x, y
        y -= 1
        count += 1

    # right
    for i in range(segment_size):
        if count == target:
            return x, y
        x += 1
        count += 1


def cells_in_layer(layer):
    if layer == 0:
        return 1
    else:
        return 8 * layer


if __name__ == '__main__':
    main()
