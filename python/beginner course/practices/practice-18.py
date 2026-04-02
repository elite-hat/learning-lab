kmap = [
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4],
    [0, 2, 4, 6, 8],
    [0, 3, 6, 9, 12],
    [0, 4, 8, 12, 16]
]
x = 0
y = 0
for row in kmap:
    if y > 4:
        y = 0
    for item in row:
        print(f"{x} * {y} = {item}")
        y += 1
    x += 1