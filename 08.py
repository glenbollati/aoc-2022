#!/usr/bin/python3
import os

lines = open("08.txt").readlines()
grid = [[int(x) for x in line.strip('\n')] for line in lines]

# grid is a square
glen = len(grid)

def is_visible(row, col, val):
    if row == 0 or col == 0 or row == glen - 1 or col == glen - 1: # edges
        return int(True)

    left   = [grid[row][x] for x in range(col - 1, -1, -1) if grid[row][x] >= val]
    right  = [grid[row][x] for x in range(col + 1, glen)   if grid[row][x] >= val]
    top    = [grid[x][col] for x in range(row - 1, -1, -1) if grid[x][col] >= val]
    bottom = [grid[x][col] for x in range(row + 1, glen)   if grid[x][col] >= val]

    return int(not len(left) or not len(right) or not len(top) or not len(bottom))

def score_tree(row, col, val):
    if row == 0 or col == 0 or row == glen - 1 or col == glen - 1: # edges
        return 0

    score = 1
    for i in range(col - 1, -1, -1):
        if grid[row][i] >= val or i == 0:
            score *= (col - i)
            break

    for i in range(col + 1, len(grid)):
        if grid[row][i] >= val or i == glen - 1:
            score *= (i - col)
            break

    for i in range(row - 1, -1, -1):
        if grid[i][col] >= val or i == 0:
            score *= (row - i)
            break

    for i in range(row + 1, len(grid)):
        if grid[i][col] >= val or i == glen - 1:
            score *= (i - row)
            break

    return score

def solve():
    vis_count = 0
    max_vis = 0
    for row in range(glen):
        for col in range(glen):
            vis_count += is_visible(row, col, grid[row][col])
            max_vis = max(max_vis, score_tree(row, col, grid[row][col]))

    print(vis_count) # 1870
    print(max_vis)   # 517440

solve()
