

import random

sequence = ("A", "B", "C", "D", "E")
print(random.choice(sequence))  #picks one     

print(random.randrange(1, 5))   #picks one     

numbers = [1, 4, 9, 84, 585, 5434]
print("Before shuffle:", numbers)

random.shuffle(numbers)# shuffles
print("After shuffle:", numbers)