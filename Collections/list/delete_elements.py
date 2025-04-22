# they are ordered , changeable(mutable), and allow duplicate values.
# the index start from 0
my_list1=[2,3,4,"Hello",2,"James","Beatrice"]
# also create a list
my_list2=list((2,3,4,"Hello",2,"James","Beatrice"))

""" TO DELETE ELEMENTS IN A LIST WE USE POP(),CLEAR(),DEL ,REMOVE()"""

# .POP() -REMOVES THE LAST ELEMENT ELSE SPECIFY THE INDEX

del_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(del_list)
del_list.pop()
print(del_list)
del_list.pop(1)
print(del_list)

# REMOVE -GIVE THE VALUE
del_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
del_list.remove("Monday")
print(del_list)
del_list.remove("Sunday")
print(del_list)

# del
de_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
del de_list[2]
print(de_list)
del de_list
# print(de_list) will rise an erro since we deleted the list

#CLEAR 
del_list.clear()
print(del_list)




