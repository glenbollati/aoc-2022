#!/usr/bin/python3
import os

def parse(line):
    direction, count = line.split()
    if direction == 'L':
        d = [0, -1]
    elif direction == 'R':
        d = [0, 1]
    elif direction == 'D':
        d = [-1, 0]
    else:
        d = [1, 0]

    return d, int(count)

def tail_path(head, tail):
    move = [0, 0]
    if abs(head[0] - tail[0]) < 2 and abs(head[1] - tail[1]) < 2:
        return move

    move[0] = 0 if head[0] == tail[0] else 1 if head[0] > tail[0] else -1
    move[1] = 0 if head[1] == tail[1] else 1 if head[1] > tail[1] else -1
    return move

def solve(segments):
    visited = {(0,0)}
    rope = [[0, 0] for i in range(segments)]
    for line in lines:
        d, c = parse(line)
        for i in range(c):
            rope[0] = [rope[0][0] + d[0], rope[0][1] + d[1]]
            for j in range(1, len(rope)):
                m = tail_path(rope[j - 1], rope[j])
                rope[j] = [rope[j][0] + m[0], rope[j][1] + m[1]]
                if j == segments - 1:
                    visited.add(tuple(rope[j]))
    print(len(visited))

lines = open("09.txt").readlines()
solve(2)  # 5981
solve(10) # 2352
