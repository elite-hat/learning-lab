# Dice
#    - Roll()

class Dice:
    def roll(self):
        import random
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return f"({x}, {y})"
    
dice = Dice()
rollResult = dice.roll()
print(rollResult)

# Solution

# class Dice:
#     def roll(self):
#         import random
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
# dice = Dice()
# (dice.roll())