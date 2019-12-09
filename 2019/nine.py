#!/usr/bin/env python3
import five as intcode


def main():
    code = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
    machine = intcode.run(code)
    outs = []
    while True:
        try:
            out = next(machine)
            outs.append(out)
        except StopIteration as e:
            break
    print(outs)
    assert(outs == code)

    code = [1102,34915192,34915192,7,4,7,99,0]
    machine = intcode.run(code)
    out = next(machine)
    print(f'16 digit number {out}')
    assert(len(str(out)) == 16)

    code = [104,1125899906842624,99]
    machine = intcode.run(code)
    assert(next(machine) == 1125899906842624)

    print('pass')

    boost_code = intcode.input_ints('9.in')
    machine = intcode.run(boost_code)
    next(machine)
    outs = [machine.send(2)]
    while True:
        try:
            out = next(machine)
            outs.append(out)
        except StopIteration as e:
            print('stopping iteration', e)
            break
    print(outs)


if __name__ == '__main__':
    main()
