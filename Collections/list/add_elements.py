my_list1=[2,3,4,"Hello",2,"James","Beatrice"]

my_list2=list((2,3,4,"Hello",2,"James","Beatrice"))

"""  ADDING ELEMENTS IN LIST WE USE APPEND( VALUE),EXTNDED() , OR INSERT(INDEX,VALUE) USING THE INDEX   POSITIONS """

## APPEND() - can only append one at a a time

my_list1.append("keep it up")
print(my_list1)

my_list1.append("Heroes")
print(my_list1)


## insert -using index
my_list1.insert(2,"Well !") # index 2
print(my_list1)

# exted two lists 
my_list1=[2,3,4,"Hello",2,"James","Beatrice"]
# also create a list
my_list2=list((2,3,4,"Hello",2,"James","Beatrice"))
my_list1.extend(my_list2)
print(my_list1)
