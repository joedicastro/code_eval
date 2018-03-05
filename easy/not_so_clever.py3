#!/usr/bin/env python3
# encoding: utf-8

"""
Not So Clever

Challenge Description:

Imagine that you have to arrange items in a certain order: pencils
from black to white in a color palette, photographs by the date taken,
banknotes from the highest to the lowest, etc. To do this, you
definitely don’t need to use the Stupid sort algorithm.

not_so_clever.gif

After each action, you need to come back to the beginning and start
all over again. Not so clever, is it? But, you need to know about this
algorithm, that’s why it is used in this challenge.

Input Sample:

The first argument is a path to a file. Each line includes a test case
which contains numbers that you need to sort using the Stupid sort
algorithm. There is also a number of iterations for an algorithm to
carry out. The numbers themselves and the number of iterations are
separated by a pipeline '|'.

4 3 2 1 | 1
5 4 3 2 1 | 2

Output Sample:

Print sorted numbers after they pass the required number of
iterations. One iteration of this sort is a pass to the moment of
making changes. Once changing the order of the digits, passing starts
from the very beginning. Hence, this is another iteration.

3 4 2 1
4 3 5 2 1

Constraints:

The number of iterations can be from 1 to 8.
One iteration of this sort is a pass to the moment of making changes.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    numbers = [int(i) for i in test.split(' | ')[0].split()]
    iterations = int(test.split(' | ')[1])
    i = 0
    while i < len(numbers) - 1 and iterations > 0:
        sort = numbers[i + 1] < numbers[i]
        if sort:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            iterations -= 1
            i = 0
        else:
            i += 1
    print(' '.join(str(i) for i in numbers))
