from convertor.main import process, display, category_options, unit_options, categories

print("\nDYNAMIC UNIT CONVERTOR")

category_options()
print("\nEnter the category from the above. Write as it is written.")

while True:
    category = input("Category: ")
    if category in categories:
        break
    else:
        print("Invalid Input")

print("\nEnter the value to change its unit: ")
while True:
    try:
        value = int(input("Value: "))
        break
    except ValueError:
        print("ValueError")

unit_options(category)
print("\nEnter the unit of the value you entered.")
while True:
    convert_from = input("Convert From: ")
    if convert_from in categories[category]:
        break
    else:
        print("Invalid Input")

unit_options(category)
print("\nEnter the unit to convert your value.")
while True:
    convert_to = input("Convert To: ")
    if convert_to in categories[category]:
        break
    else:
        print("Invalid Input")

process(category, convert_from, convert_to)

print(display(value))