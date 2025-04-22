set2=set((3,5,9,0,89,1,34,76,98,90))

set2.remove(3)
print(set2)

set2.discard(5)
print(set2)

set2.pop()  # does not remove the last since its unorded
print(set2)

set2.clear()
print(set2)

del set2