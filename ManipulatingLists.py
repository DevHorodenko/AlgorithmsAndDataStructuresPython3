# List Manipulation in Python
# This script demonstrates various list operations such as concatenation, removal, searching, slicing, and sorting.

"""

list = [1,2,3]
print(list)

list = [1,"Jhon",3.14]
print(list)

"""

list = [1,2,3,4]
list1 = [5,6,7,8]
list2 = list + list1 # Concat lists

# print(list2)

list.pop(0) # removes first element from the list
list.pop(len(list) - 1) # removes last element from the list

print(list)

list.remove(2) # removes element by itself

num = 10
if num in list:
    print("Element find")
else:
    print("Element not find")

list = [1,2,3,4]
for i in list:
    print(i) # iterating in list

t_list = tuple(list) # tuple
print(type(t_list))
print(t_list)

list = [1,2,3,4] # add in the final of the list
list.append(10)
print(list)

list.insert(1, 21) # add in a position specified
print(list)

list.sort() # sort list in ascending order
print(list)

print(list[-1]) # print the last element using "slice"

print(list[1:3]) # print elements from:to

print(list[::-1]) # invert list

