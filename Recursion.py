def factorial(n):
    if(n == 0):
        return 1
    return(n * factorial(n - 1))

""""
3! = 3 * 2 * 1 = 6

factorial(3)
    3 * factorial(2) => 3 * 2 = 6
        factorial(2)
            2 * factorial(1) => 2 * 1 = 2
            factorial(1)
                1 * factorial(0) => 1 * 1 = 1
                factorial(0) = 1
"""

# fibonacci = 1, 1, 2, 3, 5, 8, 13...
def fib(x):
    if(x == 1 or x == 2):
        return 1
    return(fib(x - 1)) + (fib(x - 2))
print(fib(6))

"""

base, exp
base = 2
exp = 10
2 ** 10 = 1024

"""
def pot(base, exp):
    if(exp == 0):
        return 1
    return(base * pot(base, exp - 1))
print(pot(2,10))