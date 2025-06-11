print("Hello")

# Unique comment

"""
Multiple
line
comments
"""

n = 10

print(type(n)) 

n = None # Same as "null"

n = "Leonardo"

print(n.upper())

n = "LEONARDO"

print(n.lower())

list = [1, 2, 3, 4]

print(list)

nameList = ['Jhon', 'Leo', 'Cesar']

print(nameList)

mixedList = [2, 'Leo', 3.14]

print(mixedList)

mixedList[1] = 'Jhon'

print(mixedList)

tuple = (1,2,3) # Immutable, means it cant be modified

print(tuple)

dic = {'Leo':24, 'Jhon':26, 'Mary':19} # Map

print(dic)

name = "Leonardo"

print(len(name))

list = [1,2,3]

print(len(list))

d = {"Leo":24 , "Jhon":26}

for key in d:
    print(d[key])

num = 10

if(num % 2 == 0):
    print("Num is even")
else:
    print("Num is odd")

num = 0

while(num < 11):
    print(num)
    num = num + 1

var = 'Leo'
Var = 'Jhon'

print(var)

def isEven(num):
    if(num % 2 == 0):
        print("Num is even")
        return True
    return False

print(isEven(10))