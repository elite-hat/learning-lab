from convertor import options

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