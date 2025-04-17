# arithmetic operators

a=90
b=12
print(a+b)
print(a*b)
print(a/b)
print(a-b)
print(a%b)#modulus
print(a**b) # exponential

print(a//b)  #rounds down to the nearest while number

""" Assignment operator """
x=5
x=x+5
print(x)

x=x-2
print(x)

#comparison operator 
print("comparison operators")
p=3
z=2 
print(p==z)
print(p!=z)
print(p>z)
print(p<z)
print(p>=z)
print(p<=z)

print("Logical operators")
#logical operators
print (p<2 and z>1) #  true when both conditions are true
print(p>2 and z>1)

print (p<2 or z>1) #  true when one conditions is true or both
print(p>2 or z>1)

print (not(p<2 or z>1))


# is and is not  -Identity Operators

#not and not in -membership operator

txt =" Hello, am so determined to learn python as  fast as possible and increase my knowledge.   "
print( "Hello" in txt)

txt =" Hello, am so determined to learn python as  fast as possible and increase my knowledge.   "
print( "Hello" not in txt)


#Operator Precedence the order in which it wi be performed

print((5%2) *(4*3))