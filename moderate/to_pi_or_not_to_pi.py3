#!/usr/bin/env python3
# encoding: utf-8

"""
To Pi Or Not To Pi

Challenge Description:

As we know from our school history course, the ancient civilizations
needed π (PI) value for the mathematical calculations. In the 5th
century, the Chinese mathematicians calculated this value to seven
decimal digits by using geometrical technics. In Indian mathematics,
it was calculated to five decimal digits. As the computer science
developed, the mathematicians managed to calculate the decimal
representation of PI to over 10 trillion digits.

Surely, we do not need the PI value calculated to 10 trillion digits,
but 5000 digits sound just right. So, we need to define the number
located at the certain sequence number in PI.

pi.jpg

Input Sample:

The first argument is a path to a file. Each line includes a test
case, which comprises a number indicating the sequence number of a PI
value.

3
1
1654

Output Sample:

Print the number that is located at that sequence number.

4
3
1

Constraints:

The sequence number cannot exceed 5000.
Comma in the PI value is not a sequence number element.
The number of test cases is 30

"""

import sys
from decimal import getcontext, Decimal
from math import factorial

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

precision = 5000
getcontext().prec = precision

# using Bailey-Borwein-Plouffle (BBP) formula
# pi = sum([
#     ((Decimal(1) / 16 ** p) * (
#         (Decimal(4) / ((8 * p) + 1)) -
#         (Decimal(2) / ((8 * p) + 4)) -
#         (Decimal(1) / ((8 * p) + 5)) -
#         (Decimal(1) / ((8 * p) + 6))))
#     for p in range(precision)])


# Fabrice Bellard's algorithm
# pi = Decimal(1 / 64) * sum([
#     ((Decimal(-1) ** n) / Decimal(2 ** (10 * n))) *
#     (
#         (Decimal(-32) / Decimal(4 * n + 1)) -
#         (Decimal(1) / Decimal(4 * n + 3)) +
#         (Decimal(256) / Decimal(10 * n + 1)) -
#         (Decimal(64) / Decimal(10 * n + 3)) -
#         (Decimal(4) / Decimal(10 * n + 5)) -
#         (Decimal(4) / Decimal(10 * n + 7)) +
#         (Decimal(1) / Decimal(10 * n + 9)))
#     for n in range(precision // 4)
# ])

# # using Chudvnosky brothers' algorithm
# 14.18 digits per iteration
C = 426880 * Decimal(10005).sqrt()
pi = C * (sum([
        Decimal(
            Decimal(
                factorial(6 * i) *
                Decimal(13591409 + 545140134 * i)
            ) /
            Decimal(
                Decimal(factorial(3 * i)) *
                Decimal(factorial(i) ** 3) *
                (Decimal(-262537412640768000) ** i)
            )
        )
        for i in range(353)
    ]) ** - 1)

# print(pi)

pi_as_string = str(pi).replace('.', '')

for test in test_cases:
    print(pi_as_string[int(test) - 1])
