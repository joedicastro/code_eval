#!/usr/bin/env python3
# encoding: utf-8

"""
Without Repetitions

Challenge Description:

In a given text, if there are two or more identical characters in
sequence, delete the repetitions and leave only the first character.

For example:

Shellless mollusk lives in wallless house in wellness. Aaaarrghh!

↓

Sheles molusk lives in wales house in welnes. Aargh!

Input Sample:

The first argument is a file. The file contains a text.

For example:

But as he spake he drew the good sword from its scabbard, and smote a
heathen knight, Jusssstin of thee Iron Valley.
No matttter whom you choose, she deccccclared, I will abide by your decision.
Wwwhat is your will?
At his magic speech the ground oppened and he began the path of descent.
I should fly away and you would never see me again.

Output Sample:

Print to stdout the text in which all repetitions are deleted.

For example:

But as he spake he drew the god sword from its scabard, and smote a
heathen knight, Justin of the Iron Valey.
No mater whom you chose, she declared, I wil abide by your decision.
Wwhat is your wil?
At his magic spech the ground opened and he began the path of descent.
I should fly away and you would never se me again.

Constraints:

The text is case-sensitive: ‘a’ and ‘A’ are different characters.
The input consists of 40 text lines.
The maximum size of the text is 10 KB.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    sentence, previous = '', ''
    for letter in test:
        if letter != previous:
            sentence += letter
        previous = letter
    print(sentence)
