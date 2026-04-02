# GENERATING RANDOM VALUES

import random

for i in range(3):
    print(random.random())       # Picks a random float number between 0 and 1
for i in range(3):
    print(random.randint(10, 20))

members = ["John", "Mary", "Bob", "Mosh"]
leader = random.choice(members)
print(leader)