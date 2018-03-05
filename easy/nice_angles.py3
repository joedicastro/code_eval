#!/usr/bin/env python3
# encoding: utf-8

"""
Nice Angles

Challenge Description:

Write a program that outputs the value of angle, reducing its
fractional part to minutes and seconds.

Input Sample:

The first argument is a path to a file that contains the values of
angles with their decimal fractions:

330.39991833
0.001
14.64530319
0.25
254.16991217

Output Sample:

Print to stdout values of angles with their fractional parts reduced
to minutes and seconds.

The whole and fractional parts are separated by period, minutes are
separated by apostrophe, seconds by double quotes. The values of
minutes and seconds are shown as two numbers (with leading zeros if
needed).

330.23'59"
0.00'03"
14.38'43"
0.15'00"
254.10'11"

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    integer_part, fractional_part = test.split('.')
    integer = int(integer_part)
    fractional = float('0.{0}'.format(fractional_part))
    minutes = int(fractional * 60)
    seconds = int(abs(minutes - (fractional * 60)) * 60)
    print('{0}.{1:02}\'{2:02}"'.format(integer, minutes, seconds))
