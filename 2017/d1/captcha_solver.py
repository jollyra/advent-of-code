#! /usr/bin/env python3


def main():
    print(solve(input().strip()))


def solve(captcha):
    count = 0
    size = len(captcha)
    offset = size // 2
    for i, digit in enumerate(captcha):
        if captcha[i] == captcha[(i + offset) % size]:
            count += int(captcha[i])
    return count


if __name__ == '__main__':
    main()
