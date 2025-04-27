#lambda arguments : expression

x=lambda a:a +5
print(x(5))

p= lambda a , b :a * b
print(p(5,6))

y= lambda a :a+9
print(y(4))

## functions of lambda 

def count(n):
    return lambda a: a * n
double=count(2)
triple=count(3)

print(double(11))
print(triple(11))