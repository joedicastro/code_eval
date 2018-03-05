#!/usr/bin/env python3
# encoding: utf-8

"""
Testing

Challenge Description:

In many teams, there is a person who tests a project, finds bugs and
errors, and prioritizes them.  Now, you have the unique opportunity to
try yourself as a tester and test a product. Here, you have two
strings - the first one is provided by developers, and the second one
is mentioned in design. You have to find and count the number of bugs,
and also prioritize them for fixing using the following statuses:
'Low', 'Medium', 'High', 'Critical' or 'Done'.

Input Sample:

The first argument is a path to a file. Each line includes a test case
with two strings separated by a pipeline '|'. The first string is the
one the developers provided to you for testing, and the second one is
from design.

Heelo Codevval | Hello Codeeval
hELLO cODEEVAL | Hello Codeeval
Hello Codeeval | Hello Codeeval

Output Sample:

Write a program that counts the number of bugs and prioritizes them for fixing using the following statuses: 

'Low' - 2 or fewer bugs; 
'Medium' - 4 or fewer bugs; 
'High' - 6 or fewer bugs; 
'Critical' - more than 6 bugs; 
'Done' - all is done; 

Low
Critical
Done

Constraints:

Strings are of the same length from 5 to 40 characters.
Upper and lower case matters.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

severity = {
    0: 'Done',
    1: 'Low',
    2: 'Low',
    3: 'Medium',
    4: 'Medium',
    5: 'High',
    6: 'High',
}

for test in test_cases:
    testing, design = test.split(' | ')
    bugs = sum([1 for i in list(zip(testing, design)) if i[0] != i[1]])
    print('Critical' if bugs > 6 else severity[bugs])
