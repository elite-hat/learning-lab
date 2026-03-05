# Write a program to remove the duplicates in a list

input = [0, 2, 4, 6, 2, 3, 5, 7, 1, 4]
output = []

print(input)

for number in input:
    if number not in output:
        output.append(number)
    else:
        output.remove(number)
print(output)