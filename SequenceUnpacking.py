# Sequence Unpacking in Python
# This script demonstrates unpacking lists, tuples, and function returns into variables.

list = [1,2,3]
a, b, c = list # unpack list

print(a)
print(b)
print(c)

t_list = (1,2,3)
a, b, c = t_list # unpack tuple

print(a)
print(b)
print(c)

list = [1,2,3]
a, _, b = list # saying that the second value inst necessary

print(a)
print(b)

name = "Leo"
c1, c2, _ = name # Getting values from a string

print(c1)
print(c2)

def func(x,y):
    return x**2, y**2 # Showing that one function can return two values

r1, r2 = func(2,3) # unpacking returns of a tuple from a function
print(r1)
print(r2)

print(func(2,3)) # Printing the two values and showing that then values are in a tuple

def func1(x,y = 3): # Showing that is possible to have optional parameters
    return x**2, y**2 # Showing that one function can return two values