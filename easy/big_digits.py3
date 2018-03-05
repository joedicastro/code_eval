#!/usr/bin/env python3
# encoding: utf-8

"""
Big Digits

Challenge Description:

In this challenge you're presented with a situation in which you need
to output big symbols on devices which only support ASCII characters
and single, fixed-width fonts. To do this you're going to use
pseudo-graphics to ‘draw’ these big symbols.

Here is an example of the font with digits from 0 to 9:

-**----*--***--***---*---****--**--****--**---**--
*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-
*--*---*---**---**--****-***--***----*---**---***-
*--*---*--*-------*----*----*-*--*--*---*--*----*-
-**---***-****-***-----*-***---**---*----**---**--
--------------------------------------------------

Each pixel is marked either with asterisk ‘*’ or with minus ‘-’. Size
of a digit is 5×6 pixels.

Your task is to write a program, which outputs the numbers given to
you with the font as in the example.

Input Sample:

The first argument is a file that contains the lines with digits
sequences you need to magnify. E.g.:

3.1415926
1.41421356
01-01-1970
2.7182818284
4 8 15 16 23 42

Output Sample:

Print to stdout the magnified digits:

***----*---*-----*--****--**--***---**--
---*--**--*--*--**--*----*--*----*-*----
-**----*--****---*--***---***--**--***--
---*---*-----*---*-----*----*-*----*--*-
***---***----*--***-***---**--****--**--
----------------------------------------
--*---*-----*---*---***----*--***--****--**--
-**--*--*--**--*--*----*--**-----*-*----*----
--*--****---*--****--**----*---**--***--***--
--*-----*---*-----*-*------*-----*----*-*--*-
-***----*--***----*-****--***-***--***---**--
---------------------------------------------
-**----*---**----*----*---**--****--**--
*--*--**--*--*--**---**--*--*----*-*--*-
*--*---*--*--*---*----*---***---*--*--*-
*--*---*--*--*---*----*-----*--*---*--*-
-**---***--**---***--***--**---*----**--
----------------------------------------
***--****---*---**--***---**----*---**--***---**---*---
---*----*--**--*--*----*-*--*--**--*--*----*-*--*-*--*-
-**----*----*---**---**---**----*---**---**---**--****-
*-----*-----*--*--*-*----*--*---*--*--*-*----*--*----*-
****--*----***--**--****--**---***--**--****--**-----*-
-------------------------------------------------------
-*----**----*--****---*---**--***--***---*---***--
*--*-*--*--**--*-----**--*-------*----*-*--*----*-
****--**----*--***----*--***---**---**--****--**--
---*-*--*---*-----*---*--*--*-*-------*----*-*----
---*--**---***-***---***--**--****-***-----*-****-
--------------------------------------------------

Constraints:

Input lines are up to 16 symbols long.
Input can contain some other symbols, which should be ignored
(i.e. points, hyphens, spaces); only numbers must be printed out.

"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

lines = [
    '-**----*--***--***---*---****--**--****--**---**--',
    '*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-',
    '*--*---*---**---**--****-***--***----*---**---***-',
    '*--*---*--*-------*----*----*-*--*--*---*--*----*-',
    '-**---***-****-***-----*-***---**---*----**---**--',
    '--------------------------------------------------'
]

segments = [[lines[j][i:i+5] for i in range(0, 50, 5)] for j in range(6)]

for test in test_cases:
    digits = {str(i) for i in range(10)}
    number = ([int(i) for i in test if i in digits])
    for line in range(len(lines)):
        print(''.join(segments[line][digit] for digit in number))
