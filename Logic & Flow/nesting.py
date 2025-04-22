#nested  for loop
character =["Brave","Strong","Intelligent","Ambitious"]
names =["Kelvin","Samuel","Beatrice","Derek"]
for x in character:
    for y in names:
        print(x,y)

g=7
if g>5:
    print("Above five,")
    if g>10:
        print("and also above 10.")
    else:
        print("and also less than 10.")    


for i in range (1,10):
     if i %2 ==0:
         continue
     print(i)

