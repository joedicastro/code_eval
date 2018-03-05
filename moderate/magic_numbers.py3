#!/usr/bin/env python3
# encoding: utf-8

"""
Magic Numbers

Challenge Description:

There are two wizards, one good and one evil. The evil wizard has
captured the princess. The only way to defeat the evil wizard is to
recite a set of magic numbers. The good wizard has given you two
numbers, A and B. Find every magic number between A and B, inclusive.

A magic number is a number that has two characteristics:

1. No digits repeat.

2. Beginning with the leftmost digit, take the value of the digit and
move that number of digits to the right. Repeat the process again
using the value of the current digit to move right again. Wrap back to
the leftmost digit as necessary. A magic number will visit every digit
exactly once and end at the leftmost digit.

For example, consider the magic number 6231.

1. Start with 6. Advance 6 steps to 3, wrapping around once (6→2→3→1→6→2→3).
2. From 3, advance to 2.
3. From 2, advance to 1.
4. From 1, advance to 6.

Input Sample:

The input is a file with each line representing a test case. Each test
case consists of two integers A and B on a line, separated by
spaces. For all test cases 1 <= A <= B <= 10000.

10 100
8382 8841

Output Sample:

For each test case print all magic numbers between A and B, inclusive,
on one line, separated by spaces. If there is no magic number between
A and B, print -1.

13 15 17 19 31 35 37 39 51 53 57 59 71 73 75 79 91 93 95 97
-1

Constraints:

The number of test cases is 20.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()


def is_magic(number):
    number_as_str = str(number)
    length = len(number_as_str)
    if length != len(set(number_as_str)) or '0' in number_as_str:
        return False
    number_as_list = [int(i) for i in number_as_str]
    digit, positions = number_as_list[0], [False for i in range(length)]
    for i in positions:
        pos = number_as_list.index(digit)
        positions[pos] = True
        digit = number_as_list[(pos + digit) % length]
    return True if digit == number_as_list[0] and all(positions) else False


for test in test_cases:
    bottom, top = [int(i) for i in test.split()]
    magic_numbers = [str(i) for i in range(bottom, top + 1) if is_magic(i)]
    print(' '.join(magic_numbers) if magic_numbers else -1)
