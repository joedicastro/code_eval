#!/usr/bin/env python3
# encoding: utf-8

"""
Broken Lcd

Challenge Description:

You have a 12-digit LCD, each digit consists of 8 segments: 7 segments
to display numbers and one segment to display a decimal mark:


The number in each digit is displayed by turning segments on or
off. It can be represented as a binary 8-bit number, each bit of which
is a segment, ordered in the following binary representation:

broken_lcd_01.png

For example, number ‘4.’ (with the decimal mark turned on) corresponds
to the following binary representation:

broken_lcd_03.png

Some segments of the display are damaged and are always turned
off. Your task is to determine whether a given number can be displayed
on the damaged LCD. You can start displaying the number with the
arbitrary digit of the LCD.

broken_lcd_02.png

Input Sample:

The first argument is a filename. Each line of the file contains
binary 8-bit numbers, which represents the state of the segments,
starting from the most left digit, and the number that you must show
on the display. The binary numbers are separated by spaces, the number
to display is separated by a semicolon.

For example:

10110001 11111000 11111110 11111111 11111111 11111111 11111111 11101101 11111111 01111111 11110010 10100111;84.525784
11111111 11110110 11101111 11110111 10111110 11110110 10111011 10100111 11111100 01100100 11111101 01011110;5.57
11000010 00001111 11111111 10111111 11101011 11110011 01111110 11011111 11111111 11111111 11111001 01101110;857.71284
11111111 01110111 10111011 11001101 11111011 11101010 11110100 01001101 11011111 11111010 10010110 10111111;66.92
11111011 10010001 11111011 11111101 10011111 10111110 01111100 11011101 10111001 11111110 11101111 11110110;188.87

Every binary number represents the state of the segments in one
digit. 1 means that a segment is working and can be turned on or off,
0 means that a segment is damaged and is always turned off.

Output Sample:

Print to stdout 1 for each test case if the number can be displayed on
a given LCD, or 0 – if the number cannot be displayed. Print out one
number in a line.

For example:

1
1
1
0
0

Constraints:

The number of test cases is 100.
The damaged segments are always turned off.
The number can be displayed starting from any digit.
Every number has a decimal mark (if it is an integer, a decimal mark
is placed after the last digit).


"""

import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

digits = {
    '0': '11111100',
    '1': '01100000',
    '2': '11011010',
    '3': '11110010',
    '4': '01100110',
    '5': '10110110',
    '6': '10111110',
    '7': '11100000',
    '8': '11111110',
    '9': '11110110'
}

for test in test_cases:
    lcd, number = [i for i in test.split(';')][0].split(), test.split(';')[1]
    float, dot_pos = '.' in number, number.find('.')
    length_number = len(number.replace('.', '')) if number != '.' else len(number)

    displayable = 0
    if 0 < length_number <= 12:
        number_as_digits = [digits[i] for i in number if i != '.']

        if not float:
            number_as_digits[-1] = number_as_digits[-1][:-1] + '1'
        else:
            number_as_digits[dot_pos - 1] = number_as_digits[dot_pos - 1][:-1] + '1'

        for i in range(len(lcd) - length_number + 1):
            display_ok = []
            for j in range(len(number_as_digits)):
                lcd_int, num_int = int(lcd[i+j], 2), int(number_as_digits[j], 2)
                display_ok.append(lcd_int & num_int == num_int)
            if all(display_ok):
                displayable = 1
                break

    print(displayable)
