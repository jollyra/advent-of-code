#!/usr/bin/env python3


def main():
    assert manhattan_dist_to_origin(12) == 3
    assert manhattan_dist_to_origin(23) == 2
    assert manhattan_dist_to_origin(1024) == 31
    assert manhattan_dist_to_origin(312051) == 430
    ans = manhattan_dist_to_origin(int(input().strip()))
    print('manhattan distance to origin: {}'.format(ans))


def manhattan_dist_to_origin(spiral_index):
    layer, layer_start_index = get_layer_and_start(spiral_index)
    side_len = layer * 8 / 4
    side_midpoint = side_len // 2 - 1  # -1 for 0-indexing
    side_index = (spiral_index - layer_start_index) % side_len
    dist_to_axis1 = abs(side_index - side_midpoint)
    dist_to_axis2 = layer
    return int(dist_to_axis1 + dist_to_axis2)


def get_layer_and_start(x):
    corners = [1]
    while corners[-1] < x:
        next = corners[-1] + 8 * len(corners)
        corners.append(next)
    return len(corners) - 1, corners[-2] + 1


if __name__ == '__main__':
    main()
