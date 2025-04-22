counties=["Nairobi","Mombasa","Naivasha"]
if "Nairobi" in counties:
    print("Yes,indeed")

counties=["Nairobi","Mombasa","Naivasha"]
for x in counties:
    print(x)


# range 
counties=["Nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
for i in range(len(counties)):
    print(i)
    print(counties[i])
    print(i)
# so it prints the index and the counties one at a time since its a loop.

counties=["Nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
i=0
while i< len(counties):
    print(counties[i])
    i+=1


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

