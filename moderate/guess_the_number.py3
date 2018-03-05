#!/usr/bin/env python3
# encoding: utf-8

"""
Guess The Number

Challenge Description:

Let’s play “Guess the number” game. This game is for two players, and
it has simple rules:

* one person (master) picks an integer in a certain range (for
  example, from 0 to 100 inclusive)

* another person (you) tries to guess it in a certain number of
  attempts.

The task is facilitated by the fact that after each attempt, a master
gives you a hint whether the number is higher or lower.

A reasonable approach to this game is to use the “divide and conquer”
principle: in a range of numbers, always select a middle number. Then,
based on the received response, discard the upper or the lower half of
this range (together with the selected number) as it cannot contain
the right answer. Now, the range of numbers is halved. Again, select
the middle number. (If the number of integers in the range is even,
select the greater one out of two middle numbers.) Repeat until you
hear “Yay!” from a master — you guessed the number.

With this algorithm, you can win in at most log2 N attempts, where N
is the range size.

Game Example

Guess the number in an inclusive range 0..9, where computer is a
master (also see the diagram below):

Computer: range form 0 to 9
Player:   5
Computer: Higher!
Player:   8
Computer: Lower!
Player:   7
Computer: Yay!

guess_the_number.png

Input Sample:

The task in this challenge is to guess the number. Because you have to
use the proposed algorithm, we know all your answers in advance. Thus,
your program should take the path to the file, in which each row
stands for a different game, as first argument. At the beginning of
each line, upper bound of the range is specified (the lower bound is
0, both are included in the range). Then, master’s answers go,
separated by spaces. E.g.

100 Lower Lower Higher Lower Lower Lower Yay!
948 Higher Lower Yay!

Output Sample:

Print to stdout a single guessed number for each row. E.g.

13
593

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    top_as_str, *answers = test.split()
    top, bottom = int(top_as_str), 0
    guess = (top + bottom + 1) // 2

    for answer in answers:
        if answer == 'Yay!':
            break
        if answer == 'Lower':
            top = guess - 1
        elif answer == 'Higher':
            bottom = guess + 1
        guess = (top + bottom + 1) // 2

    print(guess)
