# map is an inbuilt usedm to change datatype
numbers=[1,2,3,4,5]
map_to_string= tuple(map(float,numbers))
print(map_to_string)

""" isinstance() ➡️ Checks the data type"""
numbers1=[1,2,3,4,5,6,7,8,9,0]
instance_check=isinstance(numbers1,str)
print(instance_check)


my_list2=[1,"hello","Beatrice",4,7,9]
my_list=[ x for x in my_list2 if isinstance(x, int) ]
print(my_list)

mylist=tuple(map(float,my_list))
print(mylist)

