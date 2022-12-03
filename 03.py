#!/usr/bin/python3
import os
import string

def prio(ch):
    if ord(ch) > 96:
        return ord(ch) - 96
    else:
        return ord(ch) - 38

def p1():
    acc = 0
    for sack in rucksacks:
        cutoff = len(sack) // 2
        c1 = sack[0:cutoff]
        c2 = sack[cutoff:]
        common = ''
        for i in c1:
            if common != '':
                break
            for j in c2:
                if i == j:
                    common = i
                    break
        p = prio(common)
        acc += prio(common)

    print(acc)

def p2():
    acc = 0
    for i in range(0, len(rucksacks), 3):
        s1 = set(rucksacks[i].strip('\n'))
        s2 = set(rucksacks[i + 1].strip('\n'))
        s3 = set(rucksacks[i + 2].strip('\n'))
        common = s1 & s2 & s3
        acc += prio("".join(common))

    print(acc)

rucksacks = open("03.txt").readlines()
p1()
p2()
