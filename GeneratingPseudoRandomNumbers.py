# Generating Pseudo-Random Numbers in Python
# This module demonstrates various ways to generate pseudo-random numbers and manipulate sequences using the random module.

import random

print(random.randrange(4)) # function randrange receives one value and it generate a value from its range

print(random.randint(1,4)) # function randint receives two value and it generate a value from its interval, including interval values

list = [1,2,3,4]
print(random.choice(list)) # function choice get a random value from the list

list = [1,2,3,4]
random.shuffle(list)
print(list) # shuffles the sequence of the list

list = [1,2,3,4]
print(random.sample(list, 3)) # get X random values from the list

print(random.random()) # generate random values from 0 to 1, including 0 and 1

print(random.uniform(1, 10)) # generate random values from X to Y, including X and Y