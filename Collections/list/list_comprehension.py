
# LIST COMPRESSION
counties=["Nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
new_list=[x for x in counties ] # output a list
print(new_list)

## Or 

[print(x) for x in counties] # not list output


##newlist = [expression for item in iterable if condition == True]
counties=["Nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
new_list=[x for x in counties if "o" in x] # cecks thos with letter 0 and outputs thems
print(new_list)


list_number=[ x for x in range(10) if x<5 ]
print(list_number)


counties=["Nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
new_list= [x for x in counties if x == "Naivasha"] 
print(new_list)

