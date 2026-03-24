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
        print(f"Hi, I am {self.name}")


john = Person("John Smith")
john.talk()

bob = Person("Bob Smith")
bob.talk()