#intersection  ($)
#Returns items that exist in both sets.

set1={2,4,9,8,6,4,1,0}
set2={1,2,0,7,4,3,6,8}

set_intersection =set1&set2
print(set_intersection)

set_intersection2=set1.intersection(set2)
print(set_intersection2)

""" UNION """

#Returns a new set with all unique items from both sets.

set_new={"Beatrice","Nzilani","Kelvin","Samuel"}
set_new2= {"Derek","Nzilani","Stephanie","Stan"}

set_union=set_new.union(set_new2) 
print(set_union)


set_union1=set_new| set_new2 
print(set_union)


#difference
# those in a but not in b
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

## z =  x-y
z = x.difference(y) 

print(z)


##symmetric_difference
#Items in either set, but not both.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y) 
#z = x ^ y
print(z)


