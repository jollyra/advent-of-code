#!/usr/bin/env python3


from collections import defaultdict


class Robot:
    def __init__(self, num):
        self.num = num
        self.chips = []
        self.high_dest = None
        self.low_dest = None

    def set_high_dest(self, dest):
        if dest is None:
            raise ValueError('dest not defined')
        self.high_dest = dest

    def set_low_dest(self, dest):
        if dest is None:
            raise ValueError('dest not defined')
        self.low_dest = dest

    def retrieve_chip(self, chip):
        self.chips.append(chip)

    def get_high_chip(self):
        return max(self.chips)

    def get_low_chip(self):
        return min(self.chips)

    def go(self):
        print(self)
        self.low_dest.append(self.get_low_chip)
        self.high_dest.append(self.get_high_chip)
        self.chips.clear()

    def ready(self):
        return True if len(self.chips) == 2 else False

    def __str__(self):
        return 'Robot #{} carrying: {} high_dest: {} low_dest: {}'.format(self.num, self.chips, self.high_dest, self.low_dest)


def init_robots(commands, output_bins):
    bots = {}
    for command in commands:
        print(command)
        command = command.split()
        if command[0] == 'value':
            value, bot_num = int(command[1]), int(command[5])
            bot = get_or_create_bot(bots, bot_num)
            bot.retrieve_chip(value)

        elif command[0] == 'bot':
            bot_num = int(command[1])
            bot = get_or_create_bot(bots, bot_num)

            if command[5] == 'output':
                out_bin_number = int(command[6])
                bot.set_low_dest(output_bins[out_bin_number])
            elif command[5] == 'bot':
                bot_num = int(command[6])
                bot = get_or_create_bot(bots, bot_num)
                import pdb; pdb.set_trace()
                bot.set_low_dest(bots[bot_num].chips)

            if command[10] == 'bot':
                bot_num = int(command[11])
                bot = get_or_create_bot(bots, bot_num)
                bot.set_high_dest(bot.chips)
            elif command[10] == 'output':
                out_bin_number = int(command[11])
                bot.set_high_dest(output_bins[out_bin_number])
    return bots


def get_or_create_bot(bots, num):
    if num in bots:
        bot = bots[num]
    else:
        bot = Robot(num)
        bots[num] = bot
    return bot


def find_first_ready_bot(bots):
    for bot in bots.values():
        if bot.ready():
            return bot


def Input(file):
    with open(file, 'r') as f:
        return [line.strip() for line in f]


def print_bots(bots):
    for bot in bots.values():
        print(bot)

if __name__ == '__main__':
    commands = Input('10_test.txt')
    output_bins = defaultdict(list)
    bots = init_robots(commands, output_bins)
    import pdb; pdb.set_trace()
    ready_bot = find_first_ready_bot(bots)
    while ready_bot:
        ready_bot.go()
        ready_bot = find_first_ready_bot(bots)


    # [print(bot) for bot in bots.values()]
    print(output_bins)
