#!/usr/bin/env python3
# encoding: utf-8

"""
String Mask

Challenge Description:

You’ve got a binary code which has to be buried among words in order
to unconsciously pass the cipher.  Create a program that would cover
the word with a binary mask. If, while covering, a letter finds itself
as 1, you have to change its register to the upper one, if it’s 0,
leave it as it is. Words are always in lower case and in the same row
with the binary mask.

Input Sample:

The first argument is a path to a file. Each row contains a test case
with a word and a binary code separated with space, inside of it. The
length of each word is equal to the length of the binary code.

For example:

hello 11001
world 10000
cba 111

Output Sample:

Print the encrypted words without binary code.

For example:

HEllO
World
CBA

Constraints:

Words are from 1 to 20 letters long.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    word, mask = test.split()
    print(''.join(i.upper() if j == '1' else i for i, j in zip(word, mask)))
