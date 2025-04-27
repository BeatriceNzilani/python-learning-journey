#A parameter is the variable listed inside the parentheses in the function definition.
#An argument is the value that is sent to the function when it is called.-the actual value you pass to the function
def greet():
    print("Hello")
greet()    # calling a function


def greet(greeting):#parameter
    print(greeting + "Jane")
greet("Hello,")# argument
greet("Morning,")  
greet("Hi,")  

# if the paramenters are not knows put * before the parameter

def greet(*friends):
    print( "My best friend is " +friends[1])
    print(friends)

greet("Mary","Denis","Emily","Innocent","David","Nancy")


# Keyword Arguments-key value

def greet(friend1,friend2,friend3):
    print("Hello " +friend2) 

greet(friend1="hellen",friend2="william",friend3="florish")


def my_meal(meal):
    for i in meal:
        print(i)

meals= "Meat","chicken","mangoes"

my_meal(meals)


def add(a,b):
    return a + b

print(add(2,3))