#! /usr/bin/env python3


import sys
from util import *
from pprint import pprint


def main(incomplete_rules, pattern, iterations):
    rules = {}
    for pat, out in incomplete_rules.items():
        pat_set = get_orientations(pat)
        for pat in pat_set:
            rules[pat] = out
    print(f'len incomplete_rules={len(incomplete_rules)} len rules={len(rules)}')

    for _ in range(iterations):
        if len(pattern) % 2 == 0:
            squares = square_chunks(pattern, 2)
            squares = transform_squares(rules, squares)
            pattern = combine_squares(squares)
        elif len(pattern) % 3 == 0:
            squares = square_chunks(pattern, 3)
            squares = transform_squares(rules, squares)
            pattern = combine_squares(squares)
        else:
            raise Exception(f'Matrix len {len(pattern)} must be divisible by 2 or 3')

    show(pattern)

    count = 0
    for row in pattern:
        for c in row:
            if c == '#':
                count += 1
    print(count)


def combine_squares(squares_mat):
    mat = []
    for row_of_squares in squares_mat:
        size = len(row_of_squares[0])
        for i in range(size):
            row = []
            for square in row_of_squares:
                row.append(square[i])
            row = cat(row)
            mat.append(row)
    return mat


def transform_squares(rules, squares):
    size = len(squares)
    for y in range(size):
        for x in range(size):
            squares[y][x] = rules[squares[y][x]]
    return squares


def square_chunks(mat, size):
    assert(len(mat) % size == 0)
    seq = []
    for y in range(0, len(mat), size):
        for x in range(0, len(mat), size):
            seq.append(square_slice(mat, x, y, size))
    squares = chunks(seq, len(mat) // size)
    return squares


def square_slice(mat, x0, y0, size):
    seq = []
    for y in range(y0, y0 + size):
        for x in range(x0, x0 + size):
            seq.append(mat[y][x])
    square = chunks(seq, size)
    square = [cat(row) for row in square]
    return tuple(square)


def get_orientations(pattern):
    rotated = [pattern]
    for i in range(3):
        rotated.append(rotate_matrix(rotated[-1]))
    flipped = []
    for pattern in rotated:
        flipped.extend(get_all_flip_orientations(pattern))
    return set(flipped)


def get_all_flip_orientations(mat):
    north_south = mat
    south_north = tuple(flip_matrix_about_x_axis(mat))
    flipped = [north_south, south_north]
    for mat in (north_south, south_north):
        flipped.append(tuple(flip_matrix_about_y_axis(mat)))
    return flipped


def flip_matrix_about_x_axis(mat):
    return mat[::-1]


def flip_matrix_about_y_axis(mat):
    return [row[::-1] for row in mat]


def rotate_matrix(pattern):
    return tuple([''.join(col[::-1]) for col in zip(*pattern)])


def show(pattern):
    print(f'size={len(pattern)}')
    for line in pattern:
        print(line)


def Input():
    rules = {}
    with open('21_input.txt', 'r') as f:
        for line in f:
            pattern, out = line.strip().split(' => ')
            pattern = tuple(pattern.split('/'))
            out = tuple(out.split('/'))
            rules[pattern] = out
    return rules


if __name__ == '__main__':
    print('')
    starting_pattern = ('.#.', '..#', '###')
    rules = Input()
    # ans = main(rules, starting_pattern, 5)
    ans = main(rules, starting_pattern, 18)

    # print('ans:', ans)

    # mat_test_2 = ['#..#', '....', '....', '#..#']
    # show(mat_test_2)
    # mat_chunked_2 = square_chunks(mat_test_2, 2)
    # square = combine_squares(mat_chunked_2)
    # show(square)
    # print()
    # mat_test_3 = ['##.##.', '#..#..', '......', '##.##.', '#..#..', '......']
    # show(mat_test_3)
    # mat_chunked_3 = square_chunks(mat_test_3, 3)
    # square = combine_squares(mat_chunked_3)
    # show(square)
