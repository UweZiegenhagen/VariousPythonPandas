# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 06:52:11 2017

@author: Uwe Ziegenhagen
"""

sum = 0
factor = -1

for i in range(1, 10000000, 2):
        sum = sum + factor * 1/i
        factor *= -1
        
print(-4*sum)
