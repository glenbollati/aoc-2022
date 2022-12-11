#!/usr/bin/python3
def p1():
    cycle = 1
    X = 1
    strengths = []
    for line in lines:
        if cycle == 20 or (cycle - 20) % 40 == 0:
            strengths.append(cycle * X)

        if line.startswith("noop"):
            cycle += 1
            continue

        V = int(line.split()[1])
        if cycle + 1 == 20 or (cycle - 19) % 40 == 0:
            strengths.append((cycle + 1) * X)

        cycle += 2
        X += V

    print(sum(strengths))

def draw_to(cycle):
    row = (cycle - 1) // 40
    col = (cycle - 1) % 40
    return row, col

def p2():
    cycle = 1
    X = 1
    CRT = []
    row = []

    for line in lines:
        row.append("#" if 2 > len(row) - (X % 39) > -2 else " ")
        if len(row) == 40:
            CRT.append(row)
            row = []

        if line.startswith("noop"):
            cycle += 1
            continue

        V = int(line.split()[1])
        cycle += 1
        row.append("#" if 2 > len(row) - (X % 39) > -2 else " ")
        if len(row) == 40:
            CRT.append(row)
            row = []

        cycle += 1
        X += V

    for row in CRT:
        print("".join(row))

lines = open("10.txt").readlines()
p1() # 16880
p2() # RKAZAJBR
