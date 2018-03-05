#!/usr/bin/env python3
# encoding: utf-8

"""
Slang Flavor

Challenge Description:

Long serious texts are boring. Write a program that will make texts
more informal: replace every other end punctuation mark (period ‘.’,
exclamation mark ‘!’, or question mark ‘?’) with one of the following
slang phrases, selecting them one after another:

1. ‘, yeah!’
2. ‘, this is crazy, I tell ya.’
3. ‘, can U believe this?’
4. ‘, eh?’
5. ‘, aw yea.’
6. ‘, yo.’
7. ‘? No way!’
8. ‘. Awesome!’

The result should be funny.

Input Sample:

The first argument is a file that contains a text.

For example:

Lorem ipsum dolor sit amet. Mea et habeo doming praesent. Te inani
utroque recteque has, sea ne fugit verterem!
Usu ei scripta phaedrum, an sed salutatus definiebas? Qui ut recteque
gloriatur reformidans. Qui solum aeque sapientem cu.
Eu nam nusquam quaestio principes.

Output Sample:

Print to stdout the results: the text with slang phrases.

For example:

Lorem ipsum dolor sit amet. Mea et habeo doming praesent, yeah! Te
inani utroque recteque has, sea ne fugit verterem!
Usu ei scripta phaedrum, an sed salutatus definiebas, this is crazy, I
tell ya. Qui ut recteque gloriatur reformidans. Qui solum aeque
sapientem cu, can U believe this?
Eu nam nusquam quaestio principes.

Constraints:

In the input text, end punctuation mark cannot come one after another
(consequent).
Input text contains 40 lines.

"""

import sys
from itertools import cycle

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

slang = cycle(
    [
        ', yeah!',
        ', this is crazy, I tell ya.',
        ', can U believe this?',
        ', eh?',
        ', aw yea.',
        ', yo.',
        '? No way!',
        '. Awesome!',
    ]
)

puntuaction = {'.', '!', '?'}

change = False

for test in test_cases:
    text = list(test)
    for i, char in enumerate(text):
        if char in puntuaction:
            if change:
                text[i] = next(slang)
            change = not change
    print(''.join(text))
