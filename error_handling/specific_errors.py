try:
    x=10/0
except ZeroDivisionError: # always use the bulid in  here
    print("You can divide by zero")    


"""

Exception Name      	What It Means
ZeroDivisionError	   Trying to divide by zero
ValueError	           Wrong value (e.g. converting letters to numbers)
TypeError	           Using the wrong type (e.g. adding a number to a string)
IndexError	           List index out of range
KeyError	           Accessing a dictionary with a missing key
FileNotFoundError	   File doesn't exist
NameError	           Using a variable that hasn’t been defined
AttributeError	       Trying to use a method or attribute that doesn't exist
ImportError	           Error importing a module
IndentationError	   Wrong indentation (spacing) in code
SyntaxError	           The code doesn't follow Python rules (grammar)
"""    