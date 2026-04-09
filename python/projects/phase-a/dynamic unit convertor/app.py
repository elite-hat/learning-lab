
print("DYNAMIC UNIT CONVERTOR")

categories = ["length", "weight", "temperature"]

i = 0
for category in categories:
    i += 1
    print(f"{i}. {category}")

while True:
    try:
        category = int(input("Pick a Category: "))
        if category in range(1, len(categories)+1):
            break
        else:
            print("Invalid Value")
    except:
        print("Invalid Value")

