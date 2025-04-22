set1={1,3,4,5,6,7,8}
print(set1)

set2=set((3,5,9,0,89,1,34,76,98,90))
print(set2)

# add is for adding one value at a time 
# update -is for extending another set full

set1.add("hello")
print(set1)

set1.update(set2)
print(set1)

# for update it also add interables
list2=["Hello","Good","Fine"]
set1.update(list2)