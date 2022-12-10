#!/usr/bin/python3
import os
import copy
import collections

Instruction = collections.namedtuple('Instruction', 'count start end')
instrs = []
starting_stacks = [[]]

def instr_from_line(line):
    tmp = line.split()
    return Instruction(int(tmp[1]), int(tmp[3]) - 1, int(tmp[5]) - 1)

def stack_crates(line):
    lvl = 0
    for i in range(0, len(line), 4):
        while len(starting_stacks) < lvl + 1:
            starting_stacks.append([])
        if not line[i+1].isspace():
            starting_stacks[lvl].append(line[i+1])
        lvl += 1

def execute_instr(stacks, instr, p2):
    if p2 and instr.count > 1:
        stacks[instr.end] = stacks[instr.start][0:instr.count] + stacks[instr.end]
        del stacks[instr.start][0:instr.count]
    else:
        for i in range(instr.count):
            stacks[instr.end].insert(0, stacks[instr.start][0])
            del stacks[instr.start][0]

def solve(stacks, p2):
    for ins in instrs:
        execute_instr(stacks, ins, p2)
    res = [s[0] for s in stacks]
    print(*res, sep = '')

lines = open("05.txt").readlines()

# gather initial stacks and instructions
for line in lines:
    if len(line) == 1 or line.strip()[0] == '1': # blank or stack numbers line
        continue
    if line[0] == 'm': # instruction
        instrs.append(instr_from_line(line))
    else: # stack row
        stack_crates(line)

solve(copy.deepcopy(starting_stacks), False) # WHTLRMZRC
solve(copy.deepcopy(starting_stacks), True)  # GMPMLWNMG
