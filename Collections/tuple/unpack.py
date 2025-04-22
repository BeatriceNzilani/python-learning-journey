tuple1 = ("apple", "banana", "cherry")

(green,yellow,red) = tuple1

print(green)
print(yellow)
print(red)

tuple2 = ("apple", "banana", "cherry","mangoes","orange","Guava")

(green,yellow,*red) = tuple2

print(green)
print(yellow)
print(red)


tuple3= ("apple", "banana", "cherry","mangoes","orange","Guava")
(green,*yellow,red) = tuple3

print(green)
print(yellow)
print(red)

for x in tuple3:
    print (x)


tuple3= ("apple", "banana", "cherry","mangoes","orange","Guava")

x= list(tuple3)
x.sort( key = str.upper)
x=tuple(x)
print(x)
for i in range(len(x)):
    print(x[i])


tuple3= ("apple", "banana", "cherry","mangoes","orange","Guava")
p= tuple3*3
print(p)

tuple3= ("apple", "banana", "cherry","mangoes","orange","Guava")
tuple2 = ("apple", "banana", "cherry","mangoes","orange","Guava")
l=tuple3+tuple2
print(l)

print(l.count("apple"))

print(l.index("cherry"))

