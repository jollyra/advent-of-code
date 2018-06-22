#!/usr/bin/env python3


from collections import defaultdict


class Robot:
    def __init__(self, num):
        self.num = num
        self.chips = []
        self.high_dest = None
        self.low_dest = None

    def set_high_dest(self, dest):
        self.high_dest = dest

    def set_low_dest(self, dest):
        self.low_dest = dest

    def retrieve_chip(self, chip):
        self.chips.append(chip)

    def get_high_chip(self):
        return max(self.chips)

    def get_low_chip(self):
        return min(self.chips)

    def __str__(self):
        return 'Robot #{} carrying: {}'.format(self.num, self.chips)


def init_robots(commands, output_bins):
    bots = {}
    for command in commands:
        command = command.split()
        if command[0] == 'value':
            value, bot_num = int(command[1]), int(command[5])
            if bot_num in bots:
                bot = bots[bot_num]
            else:
                bot = Robot(bot_num)
                bots[bot_num] = bot
            bot.retrieve_chip(value)

        elif command[0] == 'bot':
            bot_num = int(command[1])
            if bot_num in bots:
                bot = bots[bot_num]
            else:
                bot = Robot(bot_num)
                bots[bot_num] = bot

            if command[5] == 'output':
                out_bin_number = int(command[6])
                bot.set_low_dest(output_bins[out_bin_num])
            elif command[5] == 'bot':
                recieving_bot = int(command[6])
                bot.set_low_dest(bots[recieving_bot].chips)

            if command[10] == 'bot':
                recieving_bot = int(command[11])
                bot.set_low_dest(bots[recieving_bot].chips)
            elif command[10] == 'output':
                out_bin_number = int(command[11])
                bot.set_low_dest(output_bins[out_bin_num])
    return bots


def Input(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]


if __name__ == '__main__':
    commands = Input('10_test.txt')
    output_bins = defaultdict(list)
    bots = init_robots(commands, output_bins)

    [print(bot) for bot in bots.values()]

