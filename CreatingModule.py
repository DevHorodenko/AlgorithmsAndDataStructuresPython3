# Basic Mathematical Functions
# This module provides functions for calculating factorial, power, and area of a square.

def fat(n):
    if(n==0):
        return 1
    return n * fat(n-1)

def pot(base,exp):
    if(exp==0):
        return 1
    return base*pot(base, exp -1)

def squareArea(side):
    return side * side