#!/usr/bin/python3
import os
import string

# A -> X -> rock -> 1
# B -> Y -> paper -> 2
# C -> Z -> scissors -> 3

# loss -> X -> 0
# draw -> Y -> 3
# win  -> Z -> 6

def conv(c):
    if c == 'A' or c == 'X':
        return 1
    if c == 'B' or c == 'Y':
        return 2
    if c == 'C' or c == 'Z':
        return 3

def p1(lines):
    acc = 0
    for l in lines:
        opp, me = l.split()
        o, m = conv(opp), conv(me)
        if m - o == 1 or m - o == -2: # win
            out = 6
        elif m - o == 0: # draw
            out = 3
        else: # lose
            out = 0
        acc += out + m

    print(acc)

def p2(lines):
    acc = 0
    for l in lines:
        opp, trg = l.split()
        o = conv(opp)
        if trg == 'X': # lose
            me = (o - 1)
            if me == 0:
                me = 3
            acc += me
        elif trg == 'Y': # draw
            acc += o + 3
        elif trg == 'Z': # win
            me = (o + 1)
            if me == 4:
                me = 1
            acc += me + 6
        else:
            panic()

    print(acc)

lines = open("02.txt").readlines()
p1(lines)
p2(lines)
