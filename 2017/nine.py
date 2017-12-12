#! /usr/bin/env python3


from enum import Enum


class State(Enum):
    score = 1
    skip = 2
    garbage = 3


def score(stream):
    stack = []
    score = 0
    garbage_count = 0
    state = State.score
    for c in stream:
        if state is State.score:
            if c == '{':
                stack.append(c)
                score += len(stack)
            elif c == '}':
                stack.pop()
            elif c == '<':
                state = State.garbage

        elif state is State.skip:
            state = State.garbage

        elif state is State.garbage:
            if c == '!':
                state = State.skip
            elif c == '>':
                state = State.score
            else:
                garbage_count += 1
    return score, garbage_count


if __name__ == '__main__':
    assert(score('{}')[0] == 1)
    assert(score('{{{}}}')[0] == 6)
    assert(score('{{},{}}')[0] == 5)
    assert(score('{{{},{},{{}}}}')[0] == 16)
    assert(score('{<a>,<a>,<a>,<a>}')[0] == 1)
    assert(score('{{<ab>},{<ab>},{<ab>},{<ab>}}')[0] == 9)
    assert(score('{{<!!>},{<!!>},{<!!>},{<!!>}}')[0] == 9)
    assert(score('{{<a!>},{<a!>},{<a!>},{<ab>}}')[0] == 3)
    print('pass')

    assert(score('<random characters>')[1] == 17)
    assert(score('<<<<>')[1] == 3)
    assert(score('<{!>}>')[1] == 2)
    assert(score('<!!>')[1] == 0)
    assert(score('<!!!>>')[1] == 0)
    assert(score('<{o"i!a,<{i<a>')[1] == 10)
    print('pass')

    with open('9_input.txt', 'r') as f:
        stream = f.read().strip()
        score, garbage_count = score(stream)
        print('score: {}, garbage count: {}'.format(score, garbage_count))
