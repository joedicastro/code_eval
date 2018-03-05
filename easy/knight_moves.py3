#!/usr/bin/env python3
# encoding: utf-8

"""
Knight Moves

Challenge Description:

In chess, the knight moves to any of the closest squares that are not
on the same rank, file, or diagonal. Thus the move is in the “L” form:
two squares vertically and one square horizontally, or two squares
horizontally and one square vertically:

chess.png

Your task is to find all possible positions for the next move of the
knight on the empty chessboard.

Input Sample:

The first argument is a filename that contains positions of the knight
on the chessboard in the CN form, where:

C is a letter from “a” to “h” and denotes a column.
N is a number from 1 to 8 and denotes a row.
Each position is indicated in a new line.

For example:

g2
a1
d6
e5
b1

Output Sample:

Print to stdout all possible positions for the next move of the knight
ordered alphabetically.

For example:

e1 e3 f4 h4
b3 c2
b5 b7 c4 c8 e4 e8 f5 f7
c4 c6 d3 d7 f3 f7 g4 g6
a3 c3 d2

Constraints:

The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for test in test_cases:
    col, row = cols.index(test[0]), int(test[1])
    positions = [
        (col + 1, row + 2),
        (col - 1, row + 2),
        (col + 1, row - 2),
        (col - 1, row - 2),
        (col + 2, row + 1),
        (col - 2, row + 1),
        (col + 2, row - 1),
        (col - 2, row - 1),
    ]
    valid_movements = [
        k for k, v in {
            i: (i[0] in range(8) and i[1] in range(1, 9))
            for i
            in positions
        }.items()
        if v
    ]
    in_notation = [''.join([cols[i[0]], str(i[1])]) for i in valid_movements]
    print(' '.join(sorted(in_notation)))
