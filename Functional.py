# Functional Programming in Python
# This module demonstrates the use of functions, lambdas, map, filter, and reduce for functional data manipulation.

def power2(x):
    return x ** 2 # returning power raised to 2
power2_ = lambda x: x**2
print(power2_(10))

def factorial(n):
    if(n == 0):
        return 1
    return(n * factorial(n-1))
factorial_ = lambda n: n * factorial(n-1) if n > 1 else 1
print(factorial(4))

lista = [1,2,3]
m = map(lambda x: x ** 2, lista) # each element of this list is power raised to 2
for i in m:
    print(i)

import functools
print(functools.reduce(lambda x,y: x+y, [1,2,3,4]))

f = filter(lambda x: x%2 == 0, range(10))
for i in f:
    print(i)