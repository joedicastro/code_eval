#!/usr/bin/env python3
# encoding: utf-8

"""
Details

Challenge Description:

There are two details on a M*N checkered field. The detail X covers
several (at least one first cell) cells in each line. The detail Y
covers several (at least one last cell) cells. Each cell is either
fully covered with a detail or not.

For example:

details_01.png

Also, the details may have cavities (or other complex
structures). Please see example below (the detail Y is one detail):

details_02.png

The detail Y starts moving left (without any turn) until it bumps into
the X detail at least with one cell. Determine by how many cells the
detail Y will be moved.

Input Sample:

The first argument is a file with different test cases. Each test case
contains a matrix the lines of which are separated by comma. (Empty
cells are marked as ".")

For example:

XX.YY,XXX.Y,X..YY,XX..Y
XXX.YYYY,X...Y..Y,XX..YYYY,X.....YY,XX....YY
XX...YY,X....YY,XX..YYY,X..YYYY
XXYY,X..Y,XX.Y

Output Sample:

Print out the number of cells the detail Y will be moved.

For example:

1
1
2
0

Constraints:

The matrices can be of different M*N sizes. (2 <= M <= 10, 2 <= N <= 10)
Number of test cases is 40.

"""

import sys
import re

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    print(min([len(re.findall('X(\.*)Y', i)[0]) for i in test.split(',')]))
