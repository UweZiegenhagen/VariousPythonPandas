# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 12:09:37 2017

@author: Uwe Ziegenhagen

More sophisticated rounding, direction can be set as well as the amount to be rounded to
"""

from math import ceil, floor

a = 123456789.45

def mround(x, number, direction):
    if direction=='up':
        return int(ceil(x / float(number))) * number
    else:
        return int(floor(x / float(number))) * number

print('1d ', mround(123456789.45, 10, 'up'))
print('1u ', mround(123456789.45, 10, 'down'))

print('2d ', mround(123456789.45, 100, 'up'))
print('2u ', mround(123456789.45, 100, 'down'))

print('25000d', mround(123456789.45, 25000, 'up'))
print('25000u', mround(123456789.45, 25000, 'down'))