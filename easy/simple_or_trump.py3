#!/usr/bin/env python3
# encoding: utf-8

"""
Simple Or Trump

Challenge Description:

First playing cards were invented in Eastern Asia and then spread all
over the world taking different forms and appearance. In India,
playing cards were round, and they were called Ganjifa. In medieval
Japan, there was a popular Uta-garuta game, in which shell mussels
were used instead of playing cards.

In our game, we use playing cards that are more familiar nowadays. The
rules are also simple: an ace beats a deuce (2) unless it is a trump
deuce.

Input Sample:

The first argument is a path to a file. Each line includes a test case
which contains two playing cards and a trump suit. Cards and a trump
suite are separated by a pipeline (|). The card deck includes thirteen
ranks (from a deuce to an ace) of each of the four suits: clubs (♣),
diamonds (♦), hearts (♥), and spades (♠). There are no Jokers.

AD 2H | H
KD KH | C
JH 10S | C

Output Sample:

Your task is to print a card that wins. If there is no trump card,
then the higher card wins. If the cards are equal, then print both
cards.

2H
KD KH
JH

Constraints:

The card deck includes ranks from a deuce (2) to an ace, no Jokers.
If the cards are equal, then print both cards.
The number of test cases is 40.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

values = {
    '2': 2,
    '3': 3,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14,
}

for test in test_cases:
    cards_str, trump = test.split(' | ')
    cards = cards_str.split()
    scores = {
        card: int(values[card[:-1]]) + (20 if card[-1] == trump else 0)
        for n, card
        in enumerate(cards)
    }
    winner = max(scores.values())
    print(' '.join(k for k, v in scores.items() if v == winner))
