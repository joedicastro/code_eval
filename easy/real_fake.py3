#!/usr/bin/env python3
# encoding: utf-8

"""
Real Fake

Challenge Description:

The police caught a swindler with a big pile of credit cards. Some of
them are stolen and some are fake. It would take too much time to
determine which ones are real and which are fake, so you need to write
a program to check credit cards.
To determine which credit cards are real, double every third number
starting from the first one, add them together, and then add them to
those figures that were not doubled. If the total sum of all numbers
is divisible by 10 without remainder, then this credit card is real.

Input Sample:

The first argument is a path to a file. Each row includes a test case
with a credit card number that you need to check.

9999 9999 9999 9999
9999 9999 9999 9993

Output Sample:

If a credit card is fake – print Fake, if it’s real – print Real.

Fake
Real

Constraints:

The credit card number is 16 digits in length.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    card_number = [int(i) for i in test.replace(' ', '')]
    each_third = sum(
        card_number[i] * 2
        for i, j
        in enumerate(card_number)
        if i in range(0, 16, 2)
    )
    rest = sum(
        card_number[i]
        for i, j
        in enumerate(card_number)
        if i not in range(0, 16, 2)
    )
    print('Real' if ((each_third + rest) % 10) == 0 else 'Fake')
