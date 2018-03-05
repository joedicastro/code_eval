#!/usr/bin/env python3
# encoding: utf-8

"""
Suggest Groups

Challenge Description:

You may have noticed that a new feature was added to our web site –
user groups. So, this challenge is about joining groups.

You are given a list of users of a social network, friends of each
user, and groups the user participates in.

To help users find the most interesting groups, we suggest them
joining the groups where ≥50% of their friends participate.

Your task is to write a program which finds a list of suggested groups
for each user.

Input Sample:

The first argument is a file that contains the information about each
user, one user per line. The line is delimited by colon ‘:’ into three
parts: user name, list of friends, and list of groups. The items in
each part are delimited by comma ‘,’.

For example:

Amira:Isaura,Lizzie,Madalyn,Margarito,Shakira,Un:Driving,Mineral collecting
Elliot:Isaura,Madalyn,Margarito,Shakira:Juggling,Mineral collecting
Isaura:Amira,Elliot,Lizzie,Margarito,Verla,Wilford:Juggling
Lizzie:Amira,Isaura,Verla:Driving,Mineral collecting,Rugby
Madalyn:Amira,Elliot,Margarito,Verla:Driving,Mineral collecting,Rugby
Margarito:Amira,Elliot,Isaura,Madalyn,Un,Verla:Mineral collecting
Shakira:Amira,Elliot,Verla,Wilford:Mineral collecting
Un:Amira,Margarito,Wilford:
Verla:Isaura,Lizzie,Madalyn,Margarito,Shakira:Driving,Juggling,Mineral collecting
Wilford:Isaura,Shakira,Un:Driving

Output Sample:

Print to stdout the list of suggested groups for each user. The list
of users and the list of groups for each user must be sorted
alphabetically.

For example:

Isaura:Driving,Mineral collecting
Lizzie:Juggling
Madalyn:Juggling
Margarito:Driving,Juggling
Shakira:Driving,Juggling
Un:Driving,Mineral collecting

Constraints:

Number of users in input data is 200.
Number of different groups in input data is 15.
There can be users that do not participate in any group.
Friendship is mutual (if user A is a friend with user B, then user B
is a friend with user A).

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

users = {}
all_groups = set()

for test in test_cases:
    user, friends, groups = test.split(':')
    users[user] = {
        'friends': {i for i in friends.split(',') if i},
        'groups': {i for i in groups.split(',') if i}
    }
    all_groups = all_groups.union(users[user]['groups'])

for user in sorted(users.keys()):
    number_of_friends = len(users[user]['friends'])
    friend_groups = {i:0 for i in all_groups}
    for friend in users[user]['friends']:
        for group in users[friend]['groups']:
            friend_groups[group] += 1

    suggested_groups = ','.join(
        sorted(
            [
                k
                for k, v
                in friend_groups.items()
                if v >= (number_of_friends / 2) and k not in users[user]['groups']
            ]
        )
    )
    if suggested_groups:
        print('{0}:{1}'.format(user, suggested_groups))
