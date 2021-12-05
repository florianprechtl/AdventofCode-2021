import os
import re

def readInput(part_path):
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(__location__, part_path), 'r')
    return f

def readLines(input):
    return [line.strip() for line in input]

input = readInput('../input.txt')
lines = readLines(input)

x1_of_line = [None for _ in range(1000)]
y1_of_line = [None for _ in range(1000)]
x2_of_line = [None for _ in range(1000)]
y2_of_line = [None for _ in range(1000)]

# create board size 1000x1000 starting form 0,0 filled with 0s
B = [[0 for _ in range(1000)] for _ in range(1000)]

# get points
for i,line in enumerate(lines):
    m = re.search(r'(\d+),(\d+)\s->\s(\d+),(\d+)', line)
    x1 = int(m.group(1))
    y1 = int(m.group(2))
    x2 = int(m.group(3))
    y2 = int(m.group(4))

    rangeX = range(x1, x2 + 1) or range(x2, x1 + 1)
    rangeY = range(y1, y2 + 1) or range(y2, y1 + 1)

    if x1 != x2 and y1 != y2:
        # diagonal
        pass
    elif x1 != x2 and y1 == y2:
        # vertical
        y = y1
        for x in rangeX:
            B[x][y] += 1   
    elif x1 == x2 and y1 != y2:
        #horizontal
        x = x1
        for y in rangeY:
            B[x][y] += 1   
    else:
        print("position stays the same")

# count all array entries > 1
result = 0
for x in range(1000):
    for y in range(1000):
        if B[x][y] > 1:
            result += 1

print(result)
