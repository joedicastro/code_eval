#!/usr/bin/env python3
# encoding: utf-8

"""
Meet Cocktail Sort

Challenge Description:

Quite often we need to arrange items in a certain order: numbers in an
ascending or descending order, words – in an alphabetical order,
people – according to their height, and so on. There are many
different sorting algorithms. Some of them are quick, while others
seem to suit in a particular case only.  In this challenge, your task
is to use a cocktail sort.

meet_cocktail_sort.gif

Input Sample:

The first argument is a path to a file. Each line includes a test case
with numbers that you need to order using cocktail sort. There is also
a number of iterations for an algorithm to carry out. The numbers
themselves and the number of iterations are separated by a pipeline
'|'.

5 4 9 10 7 3 2 1 6 | 1
9 8 7 6 5 4 3 2 1 | 3

Output Sample:

Print sorted numbers after they pass the required number of
iterations. One iteration of a cocktail sort is a pass through the
list of numbers in both directions: from the beginning to the end and
from the end to the beginning.

1 4 5 9 7 3 2 6 10
1 2 3 6 5 4 7 8 9

Constraints:

The number of iterations can be from 1 to 30.
One iteration of a cocktail sort is a pass through the list of numbers
in both directions: from the beginning to the end and from the end to
the beginning.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    numbers_str, iters_str = test.split(' | ')
    numbers, iterations = [int(i) for i in numbers_str.split()], int(iters_str)
    length = len(numbers)
    start, end = 0, length
    smallest, biggest = min(numbers), max(numbers)
    for i in range(iterations):
        for j in range(start, end - 1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j + 1], numbers[j]
                if j == end and numbers[j] == biggest:
                    end -= 1
        for k in range(end - 1, start, -1):
            if numbers[k] < numbers[k-1]:
                numbers[k], numbers[k-1] = numbers[k - 1], numbers[k]
                if k == start and numbers[k] == smallest:
                    start += 1
    print(' '.join([str(i) for i in numbers]))

