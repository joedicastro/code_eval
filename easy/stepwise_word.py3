#!/usr/bin/env python3
# encoding: utf-8

"""
Stepwise Word

Challenge Description:

Print the longest word in a stepwise manner.

Input Sample:

The first argument is a path to a file. Each line contains a test case
with a list of words that have different or the same length.

For example:

cat dog hello
stop football play
music is my life

Output Sample:

Find the longest word in each line and print it in one line in a
stepwise manner. Separate each new step with a space. If there are
several words of the same length and they are the longest, then print
the first word from the list.

h *e **l ***l ****o
f *o **o ***t ****b *****a ******l *******l
m *u **s ***i ****c

Constraints:

The word length is from 1 to 10 characters.
The number of words in a line is from 5 to 15.
If there are several words of the same length and they are the
longest, then print the first word from the list.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    words = test.split()
    longest = max(len(i) for i in words)
    for word in words:
        if len(word) == longest:
            print(' '.join((i * '*' + word[i]) for i in range(longest)))
        break
