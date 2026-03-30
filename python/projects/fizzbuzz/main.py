title = 'fizz buzz'
print(title.upper())
print('Enter a range of numbers:')
n1 = int(input('Start: '))
n2 = int(input('End: '))
i = n1
while i <= n2:
    if i % 3 == 0 and i % 5 == 0:
        print('fizz buzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
    i += 1

# FIXME: This program is not working correctly.