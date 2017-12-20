#! /usr/bin/env python3


from util import *
from functools import partial
import threading
import sys
import queue


def proc(seq, pid, in_q, out_q):
    regs = reset_regs(seq)
    print(regs)
    regs['p'] = pid
    send_count = 0
    ip = 0
    print('\nstart proc', pid)
    while 0 <= ip < len(seq):
        ins = seq[ip]
        cmd = ins[0]
        arg0 = regs.get(ins[1], ins[1]) if ins[1] else None
        arg1 = regs.get(ins[2], ins[2]) if len(ins) is 3 else None
        if cmd == 'snd':
            print(ins)
            out_q.put(arg0)
            send_count += 1
        elif cmd == 'set':
            regs[ins[1]] = arg1
        elif cmd == 'add':
            regs[ins[1]] += arg1
        elif cmd == 'mul':
            regs[ins[1]] *= arg1
        elif cmd == 'mod':
            regs[ins[1]] = arg0 % arg1
        elif cmd == 'rcv':
            assert(ins[1].isalpha())
            try:
                x = in_q.get(block=True, timeout=1)
                assert(isinstance(x, int))
                print(f'recieved {x} queue size {in_q.qsize()}')
                assert(ins[1].isalpha())
                regs[ins[1]] = x
            except queue.Empty:
                print(f'pid {pid} send count is {send_count}')
                return send_count
        elif cmd == 'jgz':
            if arg0 > 0:
                ip += arg1
                continue
        else:
            raise Exception(f'unrecognized command {cmd}')

        ip += 1


def parse(instructions):
    for ins in instructions:
        if len(ins) == 3:
            try:
                ins[2] = int(ins[2])
            except ValueError:
                continue
            try:
                ins[1] = int(ins[1])
            except ValueError:
                continue
        elif len(ins) == 2:
            try:
                ins[1] = int(ins[1])
            except ValueError:
                continue
    return instructions


def reset_regs(seq):
    return {el[1]: 0 for el in seq if not isinstance(el[1], int)}


if __name__ == '__main__':
    raw = input_seqs(18)
    ins = parse(raw)

    q0 = queue.Queue(maxsize=0)
    q1 = queue.Queue(maxsize=0)

    p0 = threading.Thread(target=proc, args=(ins, 0, q0, q1))
    p1 = threading.Thread(target=proc, args=(ins, 1, q1, q0))

    p0.start()
    p1.start()
