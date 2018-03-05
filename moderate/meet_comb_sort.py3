#!/usr/bin/env python3
# encoding: utf-8

"""
Meet Comb Sort

Challenge Description:

Comb sort is a simplified sorting algorithm, an improvement of a
bubble sort algorithm. It competes in speed with a well-known quick
sort algorithm.
The main idea of this sorting algorithm is that a gap between elements
can be more than 1.
Such algorithm is used in this challenge.

meet_comb_sort.gif

Input Sample:

The first argument is a path to a file. Every row includes a test case
with numbers that you need to sort using comb sort algorithm.

3 1 2
5 4 3 2 1

Output Sample:

Count and print number of iterations it will take to sort the test
case using comb sort. Iteration is a pass through the list of numbers
using the same range between the compared elements. When a pass starts
from the beginning – it’s a new iteration. If a range is, for example,
3, then take elements 0 and 3, then 1 and 4 etc.

2
3

Constraints:

Decrease factor for the algorithm is 1.25; round the result to a
smaller number.
If a range is, for example, 3, then take elements 0 and 3, then 1 and
4 etc.
One iteration for this algorithm is a pass through the list of numbers
to the end using the same range between the compared elements.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    numbers = [int(i) for i in test.split()]
    iterations, factor  = 0, 1.25
    list_sorted = False
    comb = int(len(numbers) // factor)
    while not list_sorted:
        if comb <= 1:
            list_sorted = True
        for i in range(len(numbers) - comb):
            if numbers[i] > numbers[i + comb]:
                numbers[i], numbers[i + comb] = numbers[i + comb], numbers[i]
                list_sorted = False
        if not list_sorted:
            iterations += 1
            comb = int(comb // factor)

    print(iterations)
