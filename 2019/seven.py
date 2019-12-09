#!/usr/bin/env python3
import five as intcode
from itertools import permutations


def new_amp(prog, phase):
    prog = prog[::]
    return intcode.run(prog, phase)


def run_amps_series_once(prog, phase_seq):
    amps = [new_amp(prog, phase) for phase in phase_seq]
    signal = 0
    for i, amp in enumerate(amps):
        next(amp)
        amp.send(phase_seq[i])
        signal = amp.send(signal)
    return signal


def run_amps_series_feedback(prog, phase_seq):
    amps = [new_amp(prog, phase) for phase in phase_seq]
    signal = 0

    # init
    for i, amp in enumerate(amps):
        next(amp)
        amp.send(phase_seq[i])

    s0 = 0
    while True:
        try:
            s1 = amps[0].send(s0)
            s0 = s1
            s1 = amps[1].send(s0)
            s0 = s1
            s1 = amps[2].send(s0)
            s0 = s1
            s1 = amps[3].send(s0)
            s0 = s1
            s1 = amps[4].send(s0)
            s0 = s1
        except Exception as e:
            return s0

    return signal


def input_prog(filename):
    with open(filename, 'r') as f:
        seq = f.read().split(',')
        return [int(ds) for ds in seq]


def max_thrust_phase_seq(prog):
    results = {}
    for phase_seq in permutations(range(5), 5):
        thrust = run_amps_series_once(prog, phase_seq)
        results[thrust] = phase_seq
    t = max(results.keys())
    return results[t], t


def max_thrust_phase_seq_p2(prog):
    results = {}
    for phase_seq in permutations(range(4,10), 5):
        thrust = run_amps_series_feedback(prog, phase_seq)
        results[thrust] = phase_seq
    t = max(results.keys())
    return results[t], t


def main():
    prog = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
    assert(run_amps_series_once(prog, (4,3,2,1,0)) == 43210)
    assert(max_thrust_phase_seq(prog) == ((4,3,2,1,0), 43210))
    prog = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
    assert(max_thrust_phase_seq(prog) == ((0,1,2,3,4), 54321))
    prog = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
    assert(max_thrust_phase_seq(prog) == ((1,0,4,3,2), 65210))

    prog = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    assert(run_amps_series_feedback(prog, (9,8,7,6,5)) == 139629729)
    prog = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
            -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
            53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
    assert(run_amps_series_feedback(prog, (9,7,8,5,6)) == 18216)
    print('pass')

    prog = input_prog('7.in')
    seq, thrust = max_thrust_phase_seq(prog)
    assert(thrust == 24405)
    print(f'part 1: max ({seq}, {thrust})')

    seq, thrust = max_thrust_phase_seq_p2(prog)
    assert(thrust == 8271623)
    print(f'part 2: max ({seq}, {thrust})')


if __name__ == '__main__':
    main()
