# LIST METHODS

numbers = [5, 2, 1, 5, 7, 4]
print(numbers)

numbers2 = numbers.copy()
print(numbers2)

numbers.append(20)
print(numbers)

numbers.insert(0, 10)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.count(5))

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

print(numbers.index(2))

print(50 in numbers)

numbers.clear()
print(numbers)