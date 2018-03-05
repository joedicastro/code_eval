#!/usr/bin/env python3
# encoding: utf-8

"""
Trick Or Treat

Challenge Description:

Everyone knows what Halloween is and how children love it. Children in
costumes travel from house to house asking for treats with a phrase
"Trick or treat". After that, they divide the treats equally among
all. This year, they collected tons of candies, and need your help to
share everything equally.  You know that children receive different
number of candies depending on their costume: vampire gets 3 candies
from one house, zombie – 4 candies, and witch – 5 candies.  That is,
three children in three different costumes get 3+4+5=12 candies from
one house.

Input Sample:

The first argument is a path to a file. Each line includes a test case
with number of vampires, zombies, witches, and houses that they
visited.

For example:

Vampires: 1, Zombies: 1, Witches: 1, Houses: 1
Vampires: 3, Zombies: 2, Witches: 1, Houses: 10

Output Sample:

You need to print number of candies that each child will get. If the
number is not integer, round it to the lower: for example, if the
resulting number is 13.666, round it to 13.

For example:

4
36

Constraints:

Number of vampires, zombies, witches, and houses can be from 0 to 100.
If the final number of candies is not integer, round it to the lower.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    vampires, zombies, witches, houses = [
        int(i.split(': ')[1])
        for i
        in test.split(', ')
    ]
    candies = int(
        ((3 * vampires + 4 * zombies + 5 * witches) * houses)
        /
        (vampires + zombies + witches)
    )
    print(candies)
