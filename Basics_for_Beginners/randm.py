

import random

sequence = ("A", "B", "C", "D", "E")
print(random.choice(sequence))       

print(random.randrange(1, 5))  

numbers = [1, 4, 9, 84, 585, 5434]
print("Before shuffle:", numbers)

random.shuffle(numbers)# shuffles
print("After shuffle:", numbers)
