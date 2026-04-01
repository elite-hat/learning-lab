#  INHERITANCE

# NOTE: inheritance is the mechanism fo reusing code. It's not limited to python.

# NOTE: Follow the rule DRY (Don't Repaet Yourself)

class Mammal:
    def walk():
        print("walk")
class Dog(Mammal):
    pass
class Cat(Mammal):
    pass