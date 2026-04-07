import solve

number_range = []

print(f"Enter all the numbers you want to find the sum for. \nType `done` to evaluate the results.")
while True:
    try:
        user_number = input("> ")
        if user_number == "done":
            break
        else:
            number_range.append(int(user_number))
    except:
        print("Error")
print(solve.sum(number_range))