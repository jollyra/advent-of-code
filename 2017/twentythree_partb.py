#! /usr/bin/env python3


def is_prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    h = 0
    for b in range(107900, 124900 + 1, 17):
        if not is_prime(b):
            h += 1
    print(h)
