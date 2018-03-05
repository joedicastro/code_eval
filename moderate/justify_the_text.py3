#!/usr/bin/env python3
# encoding: utf-8

"""
Justify The Text

Challenge Description:

Write a program that reformats the text into lines of 80 symbols by
stretching the text to full line width by adding spaces.

Longer series of spaces should go first. For example:

* if you need to add just one space, add it between the first and
the second word

* if there are 4 words in a line, and you need 10 spaces to stretch the
text up to 80 symbols, add 4 spaces between the first and the second
word, 3 spaces between the second and the third word, and 3 spaces
between the third and the fourth word.

The last line of the paragraph remains unchanged.

Input Sample:

The first argument is a filename. The input file contains a text.

For example:

Hello, World!
The precise 50-digits value of Pi is 3.14159265358979323846264338327950288419716939937510.
But he who would be a great man ought to regard, not himself or his interests, but what is just, whether the just act be his own or that of another. Next as to habitations. Such is the tradition.

Output Sample:

Print to stdout the text, reformatted into lines of 80 symbols by
stretching the text to the full line width by adding spaces.

For example:

Hello, World!
The         precise         50-digits        value        of        Pi        is
3.14159265358979323846264338327950288419716939937510.
But  he  who would be a great man ought to regard, not himself or his interests,
but what is just, whether the just act be his own or that of another. Next as to
habitations. Such is the tradition.

"""

import os
import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
    if len(test) <= 80:
        print(test)
    else:
        sentence = test.split(' ')
        justified_lines, temp_line = [], []

        while sentence:
            if len(' '.join(temp_line)) + len(sentence[0]) < 80:
                temp_line.append(sentence[0])
                sentence.remove(sentence[0])
            else:
                justified_lines.append(temp_line.copy())
                temp_line.clear()
        if temp_line:
            justified_lines.append(temp_line)

        for n, line in enumerate(justified_lines):
            length, num_spaces = sum(len(w) for w in line), len(line) - 1
            if n != len(justified_lines) - 1:
                len_space = (80 - length) // num_spaces if num_spaces else 0
                extra_spaces = (80 - length) % num_spaces if num_spaces else 0
            else:
                len_space, extra_spaces = 1, 0
            for i in range(len(line) - 1):
                line[i] += ' ' * len_space + (' ' if extra_spaces > 0 else '')
                extra_spaces -= 1
            print(''.join(line))
