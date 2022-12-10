#!/usr/bin/python3
import os

def solve(marker_len):
    for i in range(len(buf) - marker_len):
        s = set()
        for j in range(i, i + marker_len):
            s.add(buf[j])
        if len(s) == marker_len:
            print(i + marker_len)
            return

buf = input()
solve(4)
solve(14)
