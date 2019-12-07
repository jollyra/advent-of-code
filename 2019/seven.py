#!/usr/bin/env python3
import five as intcode
from itertools import permutations


def amp(prog, phase, signal):
    # print(f'phase {phase} signal {signal}')
    return intcode.run(prog[::], [phase, signal])


def run_amps_series(prog, phase_seq):
    signal = 0
    for x in phase_seq:
        signal = amp(prog, x, signal)
    return signal


def input_prog(filename):
    with open(filename, 'r') as f:
        seq = f.read().split(',')
        return [int(ds) for ds in seq]


def max_thrust_phase_seq(prog):
    results = {}
    for phase_seq in permutations(range(5), 5):
        thrust = run_amps_series(prog, phase_seq)
        results[thrust] = phase_seq
    t = max(results.keys())
    return results[t], t

def main():
    prog = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    assert(run_amps_series(prog, (4,3,2,1,0)) == 43210)
    assert(max_thrust_phase_seq(prog) == ((4,3,2,1,0), 43210))
    prog = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    assert(max_thrust_phase_seq(prog) == ((0,1,2,3,4), 54321))
    prog = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    assert(max_thrust_phase_seq(prog) == ((1,0,4,3,2), 65210))
    print('pass')

    prog = input_prog('7.in')
    seq, thrust = max_thrust_phase_seq(prog)
    print(f'part 1: max ({seq}, {thrust})')


if __name__ == '__main__':
    main()
