person ={"Name":"Betty","Age":20,"School":"TUK","Color":"Blue"}
print(person)

print(person["Name"])
print(person["Color"])

x=person.get("Name")
print(x)

y=person.keys()
print(y)

z=person.values()
print(z)

a=person.items()
print(a)


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")

print(x)