"""    SORT()  is case sensitive start with those in capital"""
## to change this
""" use str.lower"""



counties=["nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
counties.sort()
print(counties)

counties=["Nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
counties.sort()
print(counties)

countis=["nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
countis.sort( key= str.lower)
print(countis)




numbers=[2,4,6,3,8,378,3902,53,7,8,5,3]
numbers.sort()
print(numbers)

numbers.sort(reverse=True)## descending order
print(numbers)


##REVERSE
numbers=[2,4,6,3,8,378,3902,53,7,8,5,3]

numbers.reverse()
print(numbers)

counties=["Nairobi","Mombasa","Naivasha","Makueni","Nakuru"]
counties.reverse()
print(counties)

