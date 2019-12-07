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


def input(memory, modes, ip, input):
    size = 2
    opcode = memory[ip:ip+size]
    ins, addr = opcode
    memory[addr] = input
    return ip + size


def output(memory, modes, ip):
    size = 2
    opcode = memory[ip:ip+size]
    ins, arg0 = opcode
    val0 = arg0
    if modes.index(0) == position_mode:
        val0 = memory[arg0]
    return ip + size, val0


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

    if val0 < val1:
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


def run(memory, inputs):
    output = None
    ip = 0
    while ip < len(memory):
        modebits = str(memory[ip])[:-2]
        modes = Modes(modebits)
        ins_code = int(str(memory[ip])[-2:])
        # print(f'ins: {ins_code}, ip: {ip}/{len(memory)}')
        if ins_code in instructions:
            ins = instructions[ins_code]
            if ins_code == 3:
                ip = ins(memory, modes, ip, inputs.pop(0))
            elif ins_code == 4:
                ip, output = ins(memory, modes, ip)
            else:
                ip = ins(memory, modes, ip)
        elif ins_code == 99:
            return output
        else:
            raise Exception(f'unrecognized instruction {ins_code} at memory address {ip}')


def main():
    assert(run([3,9,8,9,10,9,4,9,99,-1,8], [8]) == 1)
    assert(run([3,9,8,9,10,9,4,9,99,-1,8], [9]) == 0)
    assert(run([3,9,7,9,10,9,4,9,99,-1,8], [7]) == 1)
    assert(run([3,9,7,9,10,9,4,9,99,-1,8], [8]) == 0)
    assert(run([3,3,1108,-1,8,3,4,3,99], [8]) == 1)
    assert(run([3,3,1108,-1,8,3,4,3,99], [9]) == 0)
    assert(run([3,3,1107,-1,8,3,4,3,99], [7]) == 1)
    assert(run([3,3,1107,-1,8,3,4,3,99], [8]) == 0)
    assert(run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [0]) == 0)
    assert(run([3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9], [1]) == 1)
    assert(run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [0]) == 0)
    assert(run([3,3,1105,-1,9,1101,0,0,12,4,12,99,1], [1]) == 1)
    assert(run([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [7]) == 999)
    assert(run([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [8]) == 1000)
    assert(run([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99], [9]) == 1001)
    print('pass')

    memory = input_ints('5.in')
    code = run(memory, [5])
    print(f'Part 2: Diagnostic code is {code}')


if __name__ == '__main__':
    main()
