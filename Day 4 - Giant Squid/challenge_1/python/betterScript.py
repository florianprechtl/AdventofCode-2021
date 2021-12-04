import os
import sys

# credits: Jonathan Paulson: https://www.youtube.com/watch?v=JbYS3_zXN_A

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

infile = os.path.join(__location__, '../input.txt')

ans = 0
numbers = None
B = []
F = []
board = []

for line in open(infile):
    line = line.strip()
    if numbers is None:
        numbers = [int(x) for x in line.split(',')]
    else:
        if line:
         board.append([int(x) for x in line.split()])
        else:
            if board:
                B.append(board)
                board = []

B.append(board)

for b in B:
    F.append([[False for _ in range(5)] for _ in range(5)])

for num in numbers:
    for i,b in enumerate(B):
        for r in range(5):
            for c in range(5):
                if b[r][c] == num:
                    F[i][r][c] = True


        won = False
        for r in range(5):
            ok = True
            for c in range(5):
                if not F[i][r][c]:
                    ok = False
            if ok:
                won = True
        for c in range(5):
            ok = True
            for r in range(5):
                if not F[i][r][c]:
                    ok = False
        if won:
            unmarked = 0
            for r in range(5):
                for c in range(5):
                    if not F[i][r][c]:
                        unmarked += b[r][c]
            print(unmarked * num)
            sys.exit(0)


        for r, row in enumerate(b):
            for c, x in enumerate(row):
                if num == x:
                    F[i][r][c] = True