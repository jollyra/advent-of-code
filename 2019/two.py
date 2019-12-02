#!/usr/bin/env python3


def input_ints(filename):
    with open('2.in', 'r') as f:
        xs = f.read().strip().split(',')
        return [int(x) for x in xs]


def run_with_args(memory, arg0, arg1):
    memory[1] = arg0
    memory[2] = arg1
    return run(memory)


def run(memory):
    ip = 0
    while ip < len(memory):
        ins = memory[ip]
        if ins == 1:
            size = 4
            opcode = memory[ip:ip+size]
            ins, addr0, addr1, addr2 = opcode
            memory[addr2] = memory[addr0] + memory[addr1]
            ip += size
        elif ins == 2:
            size = 4
            opcode = memory[ip:ip+size]
            ins, addr0, addr1, addr2 = opcode
            memory[addr2] = memory[addr0] * memory[addr1]
            ip += size
        elif ins == 99:
            opcode = memory[ip:ip]
            return memory
        else:
            raise Exception(f'unrecognized instruction {ins} at memory address {ip}')


def part_one(memory):
    memory = run_with_args(memory, 12, 2)
    return memory[0]


def part_two(initial_memory):
    for noun, verb in [(x, y) for x in range(100) for y in range(100)]:
        mem = initial_memory.copy()
        mem = run_with_args(mem, noun, verb)
        if mem[0] == 19690720:
            return 100 * noun + verb


def main():
    assert(run([1,9,10,3,2,3,11,0,99,30,40,50]) == [3500,9,10,70,2,3,11,0,99,30,40,50])
    assert(run([1,0,0,0,99]) == [2,0,0,0,99])
    assert(run([2,3,0,3,99]) == [2,3,0,6,99])
    assert(run([2,4,4,5,99,0]) == [2,4,4,5,99,9801])
    assert(run([1,1,1,4,99,5,6,0,99]) == [30,1,1,4,2,5,6,0,99])
    print('pass')

    memory = input_ints('1.in')
    print('part 1:', part_one(memory))

    memory = input_ints('1.in')
    print('part 2:', part_two(memory))


if __name__ == '__main__':
    main()
