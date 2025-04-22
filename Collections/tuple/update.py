my_tuple=("Mombasa","Kilifi","Nairobi","Eldoret","Nakuru")
print(my_tuple)

# to change we change it to a list first

mylist =list(my_tuple)
mylist[1]="Turkana"
my_tuple=tuple(mylist)
print(my_tuple)


tuple1 =("Mombasa","Kilifi","Nairobi","Eldoret","Nakuru")
list1= ("Garissa" ,)
tuple1  += list1
print(tuple1)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

