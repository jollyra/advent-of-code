#!/usr/bin/env python3


import pdb


class Screen:
    OFF = '.'
    ON = '#'

    def __init__(self, cols, rows):
        self.grid = self.init_grid(cols, rows)

    def rect(self, cols, rows):
        for row in range(rows):
            for col in range(cols):
                self.grid[row][col] = self.ON

    def rotate_row(self, row_index, n):
        row = self.grid[row_index]
        self.grid[row_index] = self.rotate_list(row, n)

    def rotate_column(self, col_index, n):
        cols = list(zip(*self.grid))
        cols = [list(col) for col in cols]
        col = list(cols[col_index])
        cols[col_index] = self.rotate_list(col, n)
        self.grid = [list(col) for col in list(zip(*cols))]

    def rotate_list(self, l, rot):
        rot = rot % len(l)
        return l[-rot:] + l[:-rot]

    def init_grid(self, cols, rows):
        grid = []
        for i in range(rows):
            grid.append([])
            for j in range(cols):
                grid[i].append(self.OFF)
        return grid

    def show(self):
        for row in self.grid:
            for col in row:
                print(col, end='')
            print()
        print()

    def render(self, commands):
        for line in commands:
            l = line.split()
            if l[0] == 'rect':
                args = l[1].split('x')
                a = int(args[0])
                b = int(args[1])
                self.rect(a, b)
            elif l[0] == 'rotate':
                # pdb.set_trace()
                a = int(l[2].split('=')[1])
                rot = int(l[4])
                if l[1] == 'column':
                    self.rotate_column(a, rot)
                elif l[1] == 'row':
                    self.rotate_row(a, rot)
                else:
                    print("unknown command")
            else:
                print("unknown command")

    def sum_pixels(self):
        count = 0
        for row in self.grid:
            for cell in row:
                if cell == self.ON:
                    count += 1
        return count


if __name__ == '__main__':
    test_screen = Screen(7, 3)
    assert test_screen.rotate_list([1, 2, 3, 4], 2)[0] is 3
    assert test_screen.rotate_list([1, 2, 3, 4], 6)[0] is 3
    test_screen.show()
    test_screen.rect(3, 2)
    test_screen.show()
    test_screen.rotate_column(1, 1)
    test_screen.show()
    test_screen.rotate_row(0, 4)
    test_screen.show()
    test_screen.rotate_column(1, 1)
    test_screen.show()

    screen = Screen(50, 6)
    with open('8_input.txt', 'r') as f:
        commands = [line for line in f]
        screen.render(commands)
        screen.show()
        print('pixels on = {}'.format(screen.sum_pixels()))

    print('pass')
