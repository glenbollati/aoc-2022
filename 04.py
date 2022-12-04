#!/usr/bin/python3
import os

def p1(lines):
    acc = 0
    for l in limits:
        if l[0] <= l[2] and l[1] >= l[3] or l[0] >= l[2] and l[1] <= l[3]:
            acc += 1
    print(acc)

def p2(lines):
    acc = 0
    for l in limits:
        if l[0] > l[3] or l[1] < l[2]:
            continue
        acc += 1
    print(acc)

lines = open("04.txt").readlines()
limits = []
for line in lines:
    pairs = line.strip("\n").split(",")
    ll = []
    ll.append(pairs[0].split("-"))
    ll.append(pairs[1].split("-"))
    ll = [int(x) for y in ll for x in y] # flatten and convert to int
    limits.append(ll)

p1(lines) # 431
p2(lines) # 823
