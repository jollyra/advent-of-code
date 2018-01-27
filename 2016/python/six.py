#! /usr/bin/env python3


from collections import Counter


def repetition_code(messages):
    message = []
    cols = zip(*messages)
    for col in cols:
        counter = Counter(col)
        most_frequent = counter.most_common()[-1][0]
        message.append(most_frequent)
    return ''.join(message)


if __name__ == '__main__':
    with open('6_in1.txt', 'r') as f:
        messages = [line.strip() for line in f]
        message = repetition_code(messages)
        print('message: ', message)
