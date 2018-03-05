#!/usr/bin/env python3
# encoding: utf-8

"""
Strings and Arrows

Challenge Description:

You have a string composed of the following symbols: '>', '<', and
'-'. Your task is to find, count, and print to the output a number of
arrows in the string. An arrow is a set of the following symbols:
'>>-->' or '<--<<'.  Note that one character may belong to two arrows
at the same time. Such example is shown in the line #1.

Input Sample:

The first argument is a path to a file. Each line includes a test case
with a string of different length from 10 to 250 characters. The
string consists of '>', '<', and '-' symbols.

For example:

<--<<--<<
<<>>--><--<<--<<>>>--><
<-->>

Output Sample:

Print the total number of found arrows for each test case.

For example:

2
4
0

Constraints:

An arrow is a set of the following symbols: '>>-->' or '<--<<'.
One symbol may belong to two arrows at the same time.
The number of test cases is 4

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

arrows = ('>>-->', '<--<<')

for test in test_cases:
    sum = 0
    for i in range(len(test) - 4):
        segment = test[i:i+5]
        if segment in arrows:
            sum += 1
    print(sum)
