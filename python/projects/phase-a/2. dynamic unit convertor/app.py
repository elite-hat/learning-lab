from convertor import options
from convertor.main import convert

print("DYNAMIC UNIT CONVERTOR")

categories = {
    1 : "length",
    2 : "weight",
    3 : "temperature"
}

for i in categories:
    print(f"{i}. {categories[i]}")

while True:
    try:
        category = int(input("Pick a Category: "))
        if category in range(1, len(categories)+1):
            break
        else:
            print("Invalid Value")
    except:
        print("Invalid Value")

options.display(category)

while True:
    try:
        option = int(input("Pick an Option: "))
        if option in range(1, options.number_of_options()+1):
            break
        else:
            print("Invalid Value")
    except:
        print("Invalid Value")

try:
    user_input = float(input(f"Enter a value to convert: "))
    print(f"Result: {convert(user_input, category, option)}")
except:
    print("Error")