# Unit Testing Example with unittest
# This module demonstrates how to write and run unit tests for mathematical functions using Python's unittest framework.

import unittest

def fat(n):
    if(n==0):
        return 1
    return n * fat(n-1)

def pot(base,exp):
    if(exp==0):
        return 1
    return base*pot(base, exp -1)

class TestMathMethods(unittest.TestCase):

    def test_pot(self):
        self.assertEqual(1024, pot(2, 10))

    def test_pot_by0(self):
        self.assertEqual(1, pot(2, 0))

    def test_fat(self):
        self.assertEqual(24, fat(4))

unittest.main()