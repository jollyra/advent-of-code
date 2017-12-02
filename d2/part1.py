#!/usr/bin/env python3


def main():
    with open('in.txt', 'r') as f:
        sum = 0
        for line in f:
            nums = line.strip().split()
            nums = list(map(int, nums))
            sum += max(nums) - min(nums)
        print(sum)


if __name__ == '__main__':
    main()
