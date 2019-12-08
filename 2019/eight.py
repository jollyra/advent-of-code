#!/usr/bin/env python3
from collections import Counter


black = 0
white = 1
transparent = 2


def input_img(fn):
    with open(fn, 'r') as f:
        return [int(c) for c in f.read()]


def chunks(size, seq):
    return [seq[i:i + size] for i in range(0, len(seq), size)]


def checksum(img, dx, dy):
    layer_size = dx * dy
    nlayers= len(img) // layer_size
    checks = {}
    for i, layer in enumerate(chunks(layer_size, img)):
        checks[i] = Counter(layer)

    min_zeros_layer = 0
    for l, check in checks.items():
        if checks[min_zeros_layer][0] > check[0]:
            min_zeros_layer = l

    return checks[min_zeros_layer][1] * checks[min_zeros_layer][2]


def new_pixels(dx, dy):
    ps = []
    for y in range(dy):
        ps.append([transparent for _ in range(dx)])
    return ps


def get_pixel(layer, dx, x, y):
    return layer[y * dx + x]


def decode(img, dx, dy):
    layer_size = dx * dy
    nlayers= len(img) // layer_size
    layers = chunks(layer_size, img)
    layers = layers[::-1]
    pixels = new_pixels(dx, dy)
    for layer in layers:
        for y in range(dy):
            for x in range(dx):
                pixel = get_pixel(layer, dx, x, y)
                if pixel == black or pixel == white:
                    pixels[y][x] = pixel
    return pixels


def render(img, dx, dy):
    decoded = decode(img, dx, dy)
    for row in decoded:
        for pixel in row:
            if pixel == black:
                print(' ', end='')
            else:
                print(pixel, end='')
        print()


def main():
    dx, dy = 25, 6
    img = input_img('8.in')
    c = checksum(img, dx, dy)
    assert(c == 1620)
    print(f'Part 1: checksum {c}')
    render(img, dx, dy)




if __name__ == '__main__':
    main()
