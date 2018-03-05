#!/usr/bin/env python3
# encoding: utf-8

"""
Swap Numbers

Challenge Description:

Write a program that, given a sentence where each word has a single
digit positive integer as a prefix and suffix, swaps the numbers while
retaining the word in between. Words in the sentence are delimited
from each other by a space.

Input Sample:

The first argument is a path to a file. Each line of the input file
contains one test case represented by a sentence. Each word in the
sentence begins and ends with a single digit positive integer i.e. 0
through 9. Assume all characters are ASCII.

4Always0 5look8 4on9 7the2 4bright8 9side7 3of8 5life5
5Nobody5 7expects3 5the4 6Spanish4 9inquisition0

Output Sample:

For each test case, print to standard output the sentence obtained by
swapping the numbers surrounding each word, one per line.

0Always4 8look5 9on4 2the7 8bright4 7side9 8of3 5life5
5Nobody5 3expects7 4the5 4Spanish6 0inquisition9

Constraints:

The suffix and the prefix of each word may be equal.
Sentences are form 1 to 17 words long.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    print(' '.join(i[-1] + i[1:-1] + i[0] for i in test.split()))
