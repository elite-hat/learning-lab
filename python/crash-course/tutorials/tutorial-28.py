# Exceptions

try:
    age = int(input("Age: "))
    print(age)
except ValueError:
    print("Unvalid Error")