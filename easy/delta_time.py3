#!/usr/bin/env python3
# encoding: utf-8

"""
Delta Time

Challenge Description:

You are given the pairs of time values. The values are in the HH:MM:SS
format with leading zeros. Your task is to find out the time
difference between the pairs.

Input Sample:

The first argument is a file that contains lines with the time pairs.

For example:

14:01:57 12:47:11
13:09:42 22:16:15
08:08:06 08:38:28
23:35:07 02:49:59
14:31:45 14:46:56

Output Sample:

Print to stdout the time difference for each pair, one per line. You
must format the time values in HH:MM:SS with leading zeros.

For example:

01:14:46
09:06:33
00:30:22
20:45:08
00:15:11

"""

import sys
from math import modf

def to_hms(time):
    hours, minutes, seconds = (int(i) for i in time.split(':'))
    return hours, minutes, seconds


def to_decimal(hhmmss):
    hours, minutes, seconds = hhmmss
    return hours + (minutes + (seconds / 60)) / 60


def to_hhmmss(t):
    hour = int(t)
    minutes = int(modf(t)[0] * 60)
    seconds = round(modf(modf(t)[0] * 60)[0] * 60)
    return '{0:02}:{1:02}:{2:02}'.format(hour, minutes, seconds)


with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    time_a_str, time_b_str = test.split()
    time_a, time_b = to_hms(time_a_str), to_hms(time_b_str)
    print(to_hhmmss(abs(to_decimal(time_a) - to_decimal(time_b))))
