#! /usr/bin/env python3


from util import *
from collections import defaultdict
from functools import partial
import threading
import sys
import queue


def proc(seq, pid, in_q, out_q):
    regs = defaultdict(int)
    regs['p'] = pid
    send_count = 0
    ip = 0
    print('\nstart proc', pid)
    while 0 <= ip < len(seq):
        ins = seq[ip]
        cmd = ins[0]
        if cmd == 'snd':
            if isinstance(ins[1], int):
                out_q.put(ins[1])
            else:
                out_q.put(regs[ins[1]])
            send_count += 1
            ip += 1
        elif cmd == 'set':
            assert(ins[1].isalpha())
            if isinstance(ins[2], int):
                regs[ins[1]] = ins[2]
            else:
                regs[ins[1]] = regs[ins[2]]
            ip += 1
        elif cmd == 'add':
            assert(ins[1].isalpha())
            if isinstance(ins[2], int):
                regs[ins[1]] += ins[2]
            else:
                regs[ins[1]] += regs[ins[2]]
            ip += 1
        elif cmd == 'mul':
            assert(ins[1].isalpha())
            if isinstance(ins[2], int):
                regs[ins[1]] *= ins[2]
            else:
                regs[ins[1]] *= regs[ins[2]]
            ip += 1
        elif cmd == 'mod':
            assert(ins[1].isalpha())
            if isinstance(ins[2], int):
                regs[ins[1]] = regs[ins[1]] % ins[2]
            else:
                regs[ins[1]] = regs[ins[1]] % regs[ins[2]]
            ip += 1
        elif cmd == 'rcv':
            assert(ins[1].isalpha())
            try:
                x = in_q.get(block=True, timeout=1)
                assert(isinstance(x, int))
                print(f'recieved {x} queue size {in_q.qsize()}')
                assert(ins[1].isalpha())
                regs[ins[1]] = x
                ip += 1
            except queue.Empty:
                print(f'pid {pid} send count is {send_count}')
                return send_count
        elif cmd == 'jgz':
            if isinstance(ins[1], int):
                if ins[1] > 0:
                    if isinstance(ins[2], int):
                        ip += ins[2]
                    else:
                        ip += regs[ins[2]]
                else:
                    ip += 1
            else:
                assert(ins[1].isalpha())
                if regs[ins[1]] > 0:
                    if isinstance(ins[2], int):
                        ip += ins[2]
                    else:
                        ip += regs[ins[2]]
                else:
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


if __name__ == '__main__':
    raw = input_seqs(18)
    ins = parse(raw)

    q0 = queue.Queue(maxsize=0)
    q1 = queue.Queue(maxsize=0)

    p0 = threading.Thread(target=proc, args=(ins, 0, q0, q1))
    p1 = threading.Thread(target=proc, args=(ins, 1, q1, q0))

    p0.start()
    p1.start()
