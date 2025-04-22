items=["Hello,","Welcome ","To","The","Team"]
for x in items:
    print(x)


for i in range(1,10):#(start,stop -is not outputted)
    print(i)
else:
    print("completed")    

for i in range(1,10):
    if i==3:
        continue
    print(i) 


#nested loop
character =["Brave","Strong","Intelligent","Ambitious"]
names =["Kelvin","Samuel","Beatrice","Derek"]
for x in character:
    for y in names:
        print(x,y)

person = {}
person['name'] = input("Enter name: ")
person['age'] = int(input("Enter age: "))

for key in person:
    print(key, ":", person[key])


person = {}
person['name'] = input("Enter name: ")
person['age'] = int(input("Enter age: "))

for key in person:
    print(f"{key}: {person[key]}")


for key, value in person.items():
    print(f"{key}: {value}")
    print(key,value)

