#!/usr/bin/env python3
# encoding: utf-8

"""
Football

Challenge Description:

People around the world watch football matches and root for different
football teams. Some people are fans of Real Madrid, some like
Barcelona, some pull for Atletico Madrid, while others do not miss a
single match with FC Bayern Munich.  The teams would like to know
people in which countries cheer for them. So, let’s help them!

Input Sample:

The first argument is a path to a file. Each row includes a test case
with lists of countries. Lists are separated by pipelines '|'. Each
list includes football teams that people in these countries root for.

For example:

1 2 3 4 | 3 1 | 4 1
19 11 | 19 21 23 | 31 39 29

Output Sample:

For each football team, print a list of countries where people root
for them. Separate each team by a semicolon ';' and a space. All
output should be sorted.

For example:

1:1,2,3; 2:1; 3:1,2; 4:1,3;
11:1; 19:1,2; 21:2; 23:2; 29:3; 31:3; 39:3;

Constraints:

The number of countries lists can be from 3 to 20.
Each list contains a different number of football teams: from 1 to 7.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    countries = [i.split() for i in test.split(' | ')]
    teams = {int(k): [] for k in set(i for j in countries for i in j)}
    for i, country in enumerate(countries):
        for team in teams.keys():
            if str(team) in country:
                teams[team].append(str(i + 1))
    print(
        '; '.join('{0}:{1}'.format(k, ','.join(v))
                  for k, v
                  in sorted(teams.items())), end=';\n'
    )
