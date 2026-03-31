n = [1, 3, 5, 7, 9, 11, 13]
print(n)

n2 = n.copy
print(n)

n.append(15)
print(n)

n.insert(16, 17)        # 17 in the place of 16
print(n)

n.reverse()
print(n)

n.sort()
print(n)

n.remove(17)
print(n)

n.pop()
print(n)

print(n.index(5))       # Outputs the index of an item
print(n.count(5))       # Numbers of 5 in a list
print(10 in n)          # True or False

n.clear()
print(n)