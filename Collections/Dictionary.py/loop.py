person ={"name":"Betty","age":20,"School":"TUK"}
print(person)

for x in person:
    print(x)

for x in person:
    print(person[x])

for x in person.values():
  print(x)

for x in person.keys():
  print(x)

for x,y in person.items():
   print(x,y)  

person ={"name":"Betty","age":20,"School":"TUK"}
print(person)
for key in person:
   print(key ,":", person[key])

for key in person:
   print  (f"{key}:{person[key]}") 

for key,value in person.items():
   print(f"{key}:{value}")
   print(key,value)


