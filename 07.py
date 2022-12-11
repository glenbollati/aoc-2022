#!/usr/bin/python3
import collections

class Dir:
    def __init__(self, path):
        self.path = path
        self.parent = None
        self.children = {}
        self.size = 0

def add_sizes(r):
    size = r.size
    for c in r.children:
        size += add_sizes(r.children[c])
    return size

def dir_sizes(sizes, r):
    for c in r.children:
        dir_sizes(sizes, r.children[c])
    sizes.append(add_sizes(r))
    return sizes

def p1(sizes):
    print(sum([s for s in sizes if s < 100000]))

def p2(sizes):
    sizes.sort()
    total = 70000000
    need = 30000000
    have = total - sizes[-1]
    for s in sizes:
        if have + s >= need:
            print(s)
            return

lines = open("07.txt").readlines()
root = Dir("/")
curr = root

for line in lines[1:]:
    spl = line.split()
    if spl[0] == "$":
        if spl[1] == "cd":
            if spl[2] == "..":
                curr = curr.parent
            else:
                tmp = curr
                curr = curr.children[spl[2]]
                curr.parent = tmp
    elif spl[0] == "dir":
        curr.children[spl[1]] = Dir(spl[1])
    else:
        curr.size += int(spl[0])

sz = dir_sizes([], root)
p1(sz)
p2(sz)
