# Write a program to find the largest number in a list

numbers = [1, 2, 3, 4, 5, 6, 7]
maximum = numbers[0]
for i in numbers:
    if maximum < i:
        maximum = i
print(maximum)

# SOLUTION      - took hint from solution to solve.

numbers = [3, 6, 2, 8, 4, 10]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)