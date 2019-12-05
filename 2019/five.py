#!/usr/bin/env python3


def input_ints(filename):
    with open(filename, 'r') as f:
        xs = f.read().strip().split(',')
        return [int(x) for x in xs]


def addr_add (memory, modes, ip):
    size = 4
    opcode = memory[ip:ip+size]
    ins, arg0, arg1, out_addr = opcode
    if modes.index(0) == position_mode:
        val0 = memory[arg0]
    else:
        val0 = arg0
    if modes.index(1) == position_mode:
        val1 = memory[arg1]
    else:
        val1 = arg1
    memory[out_addr] = val0 + val1
    return ip + size


def addr_mul (memory, modes, ip):
    size = 4
    opcode = memory[ip:ip+size]
    ins, arg0, arg1, out_addr = opcode
    if modes.index(0) == position_mode:
        val0 = memory[arg0]
    else:
        val0 = arg0
    if modes.index(1) == position_mode:
        val1 = memory[arg1]
    else:
        val1 = arg1
    memory[out_addr] = val0 * val1
    return ip + size


def input(memory, modes, ip):
    size = 2
    opcode = memory[ip:ip+size]
    ins, addr = opcode
    memory[addr] = 5
    return ip + size


def output(memory, modes, ip):
    size = 2
    opcode = memory[ip:ip+size]
    ins, addr = opcode
    o = memory[addr]
    print(o)
    return ip + size


def jump_if_true(memory, modes, ip):
    size = 3
    opcode = memory[ip:ip+size]
    ins, arg0, arg1 = opcode

    val0 = arg0
    if modes.index(0) == position_mode:
        val0 = memory[arg0]

    val1 = arg1
    if modes.index(1) == position_mode:
        val1 = memory[arg1]

    if val0 != 0:
        return val1
    return ip + size


def jump_if_false(memory, modes, ip):
    size = 3
    opcode = memory[ip:ip+size]
    ins, arg0, arg1 = opcode

    val0 = arg0
    if modes.index(0) == position_mode:
        val0 = memory[arg0]

    val1 = arg1
    if modes.index(1) == position_mode:
        val1 = memory[arg1]

    if val0 == 0:
        return val1
    return ip + size


def equals(memory, modes, ip):
    size = 4
    opcode = memory[ip:ip+size]
    ins, arg0, arg1, out_addr = opcode

    val0 = arg0
    if modes.index(0) == position_mode:
        val0 = memory[arg0]

    val1 = arg1
    if modes.index(1) == position_mode:
        val1 = memory[arg1]

    if val0 == val1:
        memory[out_addr] = 1
    else:
        memory[out_addr] = 0
    return ip + size


def less_than(memory, modes, ip):
    size = 4
    opcode = memory[ip:ip+size]
    ins, arg0, arg1, out_addr = opcode

    val0 = arg0
    if modes.index(0) == position_mode:
        val0 = memory[arg0]

    val1 = arg1
    if modes.index(1) == position_mode:
        val1 = memory[arg1]

    if val0 > val1:
        memory[out_addr] = 1
    else:
        memory[out_addr] = 0
    return ip + size


instructions = {
    1: addr_add,
    2: addr_mul,
    3: input,
    4: output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals
}


position_mode = 0
parameter_mode = 1


class Modes:
    def __init__(self, modebits):
        self.bits = modebits[::-1]

    def index(self, i):
        if len(self.bits) > i:
            return int(self.bits[i])
        return 0


def run(memory):
    ip = 0
    while ip < len(memory):
        modebits = str(memory[ip])[:-2]
        modes = Modes(modebits)
        ins_code = int(str(memory[ip])[-2:])
        print(f'ins: {ins_code}, ip: {ip}/{len(memory)}')
        if ins_code in instructions:
            ins = instructions[ins_code]
            ip = ins(memory, modes, ip)
        elif ins_code == 99:
            return memory
        else:
            raise Exception(f'unrecognized instruction {ins_code} at memory address {ip}')


def main():
    assert(run([1002,4,3,4,33]) == [1002,4,3,4,99])
    print('pass')

    memory = input_ints('5.in')
    memory = run(memory)


if __name__ == '__main__':
    main()
