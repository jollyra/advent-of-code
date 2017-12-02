#! /usr/bin/env python3

"""
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that match the next digit in the list. The list is circular, so the digit after the last digit is the first digit in the list.
"""

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
