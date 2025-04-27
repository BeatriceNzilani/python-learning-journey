import random

print(random.randrange(1,9))
print(random.randint(1,9))
print(random.choice(["Python","JS","HTML","CSS"]))
numbers=[2,8,9,56,7,90,45,23,65]
random.shuffle(numbers)
print(numbers) 
print(random.uniform(1.7,3.0))