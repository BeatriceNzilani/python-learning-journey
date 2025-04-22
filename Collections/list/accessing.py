my_list1=[2,3,4,"Hello",2,"James","Beatrice"]

my_list2=list((2,3,4,"Hello",2,"James","Beatrice"))

# accessing
print(my_list1[3])
print(my_list1[-1])# last element
print(my_list1[2:5]) # the index five is not included in the output
print(my_list1[-5:-1])#the  last index  is not included in the output and count from 1 from the last value
print(my_list1[2:])
print(my_list1[:4])


counties=["Nairobi","Mombasa","Naivasha"]
if "Nairobi" in counties:
    print("Yes,indeed")


fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")