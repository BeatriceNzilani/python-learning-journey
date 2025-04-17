#variable is a named storage location that holds a value, which can be changed during the execution of a program.

"""
rules when writting variables
1.There is no spacing 
2.cannot start with a number - so  it starts with a letter.
3.cannot be a reserved or a keyword- word that have predefined /special meaning in the programming language.
4.Case-sensitive (e.g., myVar and myvar are different).
5.No special characters like @, #, or $ (only use letters, numbers, and underscores).
6.Use descriptive names (e.g., totalAmount, userAge).
7.Avoid using built-in function names (e.g., print, list).

"""
x=5
print(x)
x="hello"
print(x)
x=0
print(x)

                 # assigning multiple values
x,y,z= "Nzilani","learns","python"
print(x)
print(y)
print(z)

x=y=z ="learn"
print(x)
print(y)
print(z)

        #GLOBAL AND LOCAL VARIABLES -intersting!!
"""
  Global Variable: Declared outside any function,
  and it can be accessed anywhere in the program (inside functions or outside).
""" 

y=10
def glob():
    print(y)
glob()  
print(y)

"""
Local Variable: Declared inside a function, and it can only be accessed inside that function.
"""
def loc():
    l=7
    print(l)
loc()
 # print(l) -this will actually raise an error cause  l is alocal variable