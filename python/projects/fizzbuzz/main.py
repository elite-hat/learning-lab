title = "fizz buzz"
print(title.upper())
print("Enter a range of numbers.")
n1 = int(input("Start:"))
n2 = int(input("End:"))
i = n1
while i < n2:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    else:
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)