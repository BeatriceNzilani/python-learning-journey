a="""Hello
Friend
i 
really 
love 
you!!
"""
print(a)
 # string is a text type

q="Hello"
print(q)
print(type(q))

## to access elemnt of a string- we use the array []

element ="God is on my side"
print(element[1])# starts from 0
print(element[8]) # so NB  a spece is also considered like an element.


# the length and it starts counting from 1 
print(len(element))

""" CHECK STRING"""


txt ="Hello, am so determined to learn python as  fast as possible and increase my knowledge.   "
print("as" in txt) # true or false

if "Hello" in txt:
    print("yes,its present.")

if "q" not in txt:
    print("yes,it's absent. ")

    ##slicing string
print(txt[1:5])    
print(txt[:5])
print(txt[1:])
print(txt[-2])
print(txt[-9:-1])


#modifying

print(txt.upper())
print(txt.lower())
print(txt.strip())
print(txt.split("as"))
print(txt.replace("am","I'm"))
print(txt.capitalize())
print(txt.count("as"))

print(txt.casefold())