#!/usr/bin/env python3
# encoding: utf-8

"""
Matrix Rotation

Challenge Description:

You are given a 2D N×N matrix. Each element of the matrix is a letter:
from ‘a’ to ‘z’. Your task is to rotate the matrix 90° clockwise:

a b c        g d a
d e f  =>    h e b
g h i        i f c

Input Sample:

The first argument is a file that contains 2D N×N matrices, presented
in a serialized form (starting from the upper-left element), one
matrix per line. The elements of a matrix are separated by spaces.

For example:

a b c d
a b c d e f g h i j k l m n o p
a b c d e f g h i

Output Sample:

Print to stdout matrices rotated 90° clockwise in a serialized form
(same as in the input sample).

For example:

c a d b
m i e a n j f b o k g c p l h d
g d a h e b i f c

Constraints:

The N size of the matrix can be from 1 to 10
The number of test cases is 100

"""

import sys
from math import sqrt

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    elements = test.split()
    size = int(sqrt(len(elements)))
    print(' '.join(
            [' '.join(
                [elements[size * i + k] for i in range(size)][::-1])
             for k
             in range(size)
            ])
    )
