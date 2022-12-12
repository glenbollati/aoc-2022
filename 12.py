#!/usr/bin/python3
lines = open("12.test").readlines()
grid = []

for r in range(len(lines)):
    row = []
    for c in range(len(lines[r].strip("\n"))):
        char = lines[r][c]

        if char == 'S':
            start = (r, c)
            char = 'a'

        elif char == 'E':
            end = (r, c)
            char = 'z'

        row.append(ord(char) - ord('a'))

    grid.append(row)

for row in grid:
    print(row)
