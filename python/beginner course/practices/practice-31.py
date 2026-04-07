class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def talk(self):
        print(f"Hello! I'm {self.name}. Nice to meet you!")
    def introduction(self):
        print(f"I'm {self.name} a {self.age} years old {self.gender}.")

person1 = Person("Ali", "male", 20)
person1.talk()
print(person1.name)
print(person1.gender)
print(person1.age)

person2 = Person("Ahmed", "male", 25)
person2.talk()
print(person2.name)
print(person2.gender)
print(person2.age)