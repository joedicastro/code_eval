#!/usr/bin/env python3
# encoding: utf-8

"""
Locks

Challenge Description:

There are N unlocked rooms located in a row along the corridor.

A security guard, who starts the beat at the beginning of the
corridor, passes by and closes the lock of every second door (2nd,
4th, 6th…). Then he returns to the beginning of the corridor, and
passes by again changing the state of every third door (3rd, 6th,
9th…) to the opposite state — if the door is closed, security guard
opens it; if the door is open, he closes it.

One iteration consists of two beats (when the security guard closes
each second door, and changes the state of each third door to the
opposite state). The iteration repeats M-1 times.

During the last iteration, the security guard just changes the state
of the last door in a row (closes it, if the door is open or opens it,
if the door is closed).

Your task is to determine how many doors have been left unlocked.


Input Sample:

Your program accepts a filename as its first argument.

Each line of input contains 2 integers separated by space. The first
integer represents number of doors (N), the second — number of
iterations (M).

3 1
100 100

Output Sample:

For each line of input print out how many doors are left unlocked:

2
50

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    number_of_doors, iterations = [int(i) for i in test.split()]
    doors = [True for i in range(number_of_doors)]
    for i in range(iterations - 1):
        for snd in range(1, number_of_doors, 2):
            doors[snd] = False
        for trd in range(2, number_of_doors, 3):
            doors[trd] = not doors[trd]
    doors[-1] = not doors[-1]

    print(sum([1 if door else 0 for door in doors]))
