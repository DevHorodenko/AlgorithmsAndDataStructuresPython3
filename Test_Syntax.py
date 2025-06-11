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

for i in range(10):
    print(i)

list = [1,2,3]

for i in list:
    print(i)

for i in range(len(list)):
    print(list[i])
    print(i)

for i in range(1, 10, 2):
    print(i)

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setAge(self, age):
        self.age = age
    
p = Person('Leo', 24)

print('Name: %s' % p.getName())
print('Age: %d' % p.getAge())

p1 = Person('Jhon', 30)
p2 = Person('Mary', 63)

list = []
list.append(p1)
list.append(p2)

for p in list:
    print('Name: %s' % p.getName())
    print('Age: %d' % p.getAge())

print('Age before change: %d' % p1.getAge())

p1.setAge(52)

print('Age after change: %d' % p1.getAge())

listEven = [num for num in range(101) if num % 2 == 0]
print(listEven)