 
# to check the data type we use the type principle

""" Number types """
#interger
x=5 
print(x)
print(type(x))

#complex
z = 3 + 4j
print(type(z))

#float
y=8.9
print(type(y))

""" Text Type"""
""" can use single or duoble quotation """
# string
student_name = "jane"
print(type(student_name))

"""Sequence Types"""
#list 
"""LAM"""
# Ordered, mutable (changeable) collection of elements. Can contain any data type.

members= ["kelvin","Samuel","Derek","Beatrice","Stephanie"]
print(members)
print(type(members))

#tuple 
#Ordered, immutable (unchangeable) collection of elements.

team=("kelvin",1,"Samuel",2,"Derek",3,"Beatrice",4,"Stephanie")
print(team)
print(type(team))
#range
#Represents a sequence of numbers, often used for looping
numbers = range(5)
print(numbers)
print(type(numbers))

"""Mapping Type"""
#Dictionary
#Unordered collection of key-value pairs.
student={"name":"Beatrice","Age":20,"gender":"female"}
print(student)
print(type(student))

""". Set Types """
# Unordered collection of unique elements -no duplicates .
colors = {"red", "green", "blue"}
print(colors)
print(type(colors))

v = frozenset({"red", "green", "blue"})
print(v)
print(type(v))


#boolean type

f=True
print(f)
print(type(f))

import random 
print(random.randrange(1,5))
sequence=["Apple","Mango","Orange"]
print(random.choice(sequence))