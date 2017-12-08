#! /usr/bin/env python3


import sys
from collections import defaultdict, namedtuple


Ins = namedtuple('Ins', 'reg0 op val0 keyword reg1 comp val1')


def parse(lines):
    ops = {'inc': '+',
           'dec': '-'}
    instructions = []
    for line in lines:
        s = line.split()
        ins = Ins(reg0=s[0],
                  op=ops.get(s[1]),
                  val0=int(s[2]),
                  keyword=s[3],
                  reg1=s[4],
                  comp=s[5],
                  val1=int(s[6]))
        instructions.append(ins)
    return instructions


def execute(instructions, regs):
    intermediate_max = 0
    for ins in instructions:
        code = """if regs['{reg1}'] {comp} {val1}: regs['{reg0}'] {op}= {val0}""".format(
               reg0=ins.reg0,
               op=ins.op,
               val0=ins.val0,
               reg1=ins.reg1,
               comp=ins.comp,
               val1=ins.val1)
        exec(code)

        largest = sorted(regs.values(), reverse=True)[0]
        if largest > intermediate_max:
            intermediate_max = largest

    return intermediate_max


def Input():
    lines = []
    with open(sys.argv[1], 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


if __name__ == '__main__':
    regs = defaultdict(int)
    lines = Input()
    instructions = parse(lines)
    max_reg = execute(instructions, regs)
    print(max_reg)
