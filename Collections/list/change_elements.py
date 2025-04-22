my_list1=[2,3,4,"Hello",2,"James","Beatrice"]

my_list2=list((2,3,4,"Hello",2,"James","Beatrice"))


# changing 
my_list1[1] ="Well"
my_list1[1:3]=["blackcurrant", "watermelon"]
print(my_list1)

# replace one index with two elements
my_list1[1:2]=["t","y"]
print(my_list1)
# changing two index with one element
my_list1[6:8]=["Hello"]
print(my_list1)

thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)
