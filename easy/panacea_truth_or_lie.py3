#!/usr/bin/env python3
# encoding: utf-8

"""
Panacea - Truth or Lie

Challenge Description:

There are many computer and human viruses nowadays. Scientists are
scratching their heads over antiviruses that could stop a particular
virus and, in most cases, they find right solutions.  So, virologists
need to know which antiviruses can protect us from viruses, and what
they still have to work on to secure against the remaining
viruses. Let’s help them out!

Input Sample:

The first argument is a path to a file. Each line includes a test case
with virus components in the hexadecimal numeral system (HEX) and
antivirus components in the binary number system (BIN). Virus and
antivirus components are separated by a pipeline '|'.

64 6e 78 | 100101100 11110
5e 7d 59 | 1101100 10010101 1100111
93 75 | 1000111 1011010 1100010

Output Sample:

Your task is to calculate the sum of all virus components and compare
it with the sum of antivirus components. If the numbers are the same
or the sum of antivirus components is greater than the sum of virus
components, this means that the virus was stopped. So, print
True. Otherwise, print False.

True
True
False

CONSTRAINTS:

The sum of components can be from 60 to 1500.
The number of components in virus and antivirus can be from 1 to 8.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    hex_str, bin_str = test.split('|')
    hex_sum = sum(int(i, base=16) for i in hex_str.split())
    bin_sum = sum(int(i, base=2) for i in bin_str.split())
    print(bin_sum >= hex_sum)
