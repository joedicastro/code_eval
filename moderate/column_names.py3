#!/usr/bin/env python3
# encoding: utf-8

"""
Column Names

Challenge Description:

Microsoft Excel uses a special convention to name its column
headers. The first 26 columns use the letters 'A' to 'Z'. Then, Excel
names its column headers using two letters, so that the 27th and 28th
column are 'AA' and 'AB'. After 'ZZ', Excel uses three letters.

Write a function that takes as input the number of the column, and
returns its header. The input will not ask for a column that would be
greater than 'ZZZ'.

Input Sample:

The first argument is a path to a file. Each line of the input file
contains one test case represented by one integer.

52
3702

Output Sample:

For each test case your program must print one line containing the
Excel column heading corresponding to the integer in the input.

AZ
ELJ

Constraints:

1. The number of test cases is 40.
2. The input will not ask for a column that would be greater than 'ZZZ'.

"""

import sys
from itertools import product
from string import ascii_uppercase

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

headings = (
    [''.join(i) for i in product(ascii_uppercase, repeat=2)] +
    [''.join(i) for i in product(ascii_uppercase, repeat=3)]
)

for test in test_cases:
    if int(test) <= 26:
        print(ascii_uppercase[int(test) - 1])
    elif int(test) >= 27:
        print(headings[int(test) - 1 - 26])
