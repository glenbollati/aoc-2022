#!/usr/bin/python3
import os

lines = open("08.test").readlines()
grid = [[int(x) for x in line.strip('\n')] for line in lines]
print(grid)

def is_visible(row, col, val):
    if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid[0]) - 1: # edges
        return True

    # missing one here
    left   = [grid[row][x] for x in range(col - 1, -1, -1) if x > val]
    right  = [grid[row][x] for x in range(col + 1, len(grid[row])) if x > val]
    top    = [grid[x][col] for x in range(row - 1, -1, -1) if x > val]
    bottom = [grid[x][col] for x in range(row + 1, len(grid[col])) if x > val]

    return len(left) or len(right) or len(top) or len(bottom)

count = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if is_visible(row, col, grid[row][col]):
            count += 1

print(count)
