class Person:
    def talk(self):
        print('Hello')

person1 = Person()
person1.name = input('Uncle')
person1.talk()

# Solution

class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print("talk")


john = Person("John Smith")
print(john.name)
john.talk()