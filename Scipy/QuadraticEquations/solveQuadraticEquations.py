# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 13:39:44 2017

@author: Uwe Ziegenhagen
"""
from math import sqrt

def solveQuad(p, q):
    partOne = -p/2
    partTwo = sqrt((-p/2)**2 - q)
    return (partOne-partTwo,partOne+partTwo)
 
print(solveQuad(1,-1))