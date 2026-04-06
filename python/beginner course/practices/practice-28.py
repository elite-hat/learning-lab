a = 10
b = 0

try:
    print(a / b)
except ZeroDivisionError:
    print("Can't be divided by Zero")

# NOTE: ValueError can be used, when there is an invalid value.