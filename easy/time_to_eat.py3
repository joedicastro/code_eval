#!/usr/bin/env python3
# encoding: utf-8

"""
Time To Eat

Challenge Description:

It's amazing how fast time flies by and we don’t even realize it. As
we are getting older, time seems to move so much faster than it did in
the past.  Perception of time is relative to how fast our heart rate
is. An unborn baby’s heart rate is incredibly fast and as we age, it
slows. Metabolic rate of an organism determines its perception of
time. Organisms like cats and dogs have a very high metabolic rate;
thus, the breaks between their meals seem to be shorter than humans
have.  At codeeval.com, we have a cat called Kitty. She loves eating,
and it seems like she can eat anything any time. We want to keep Kitty
fit, so we feed her according to a schedule.  Planning her daily
meals, we need to see when Kitty will eat starting with the latest
meal in the evening to the earliest morning snack. So, your task is to
sort timestamps in the schedule in a reverse chronological order.

Input Sample:

The first argument is a path to a file. Each line includes a test
case: a schedule containing unsorted timestamps in HH:MM:SS format.

For example:

02:26:31 14:44:45 09:53:27
05:33:44 21:25:41

Output Sample:

Sort timestamps in each schedule from the biggest to the smallest one.

14:44:45 09:53:27 02:26:31
21:25:41 05:33:44

Constraints:

Each schedule may have from 2 to 20 timestamps.
Timestamp 23:59:59 - biggest and 00:00:01 the smallest one.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    timestamps = [i.split(':') for i in test.split()]
    print(' '.join(':'.join(i) for i in sorted(timestamps, reverse=True)))
