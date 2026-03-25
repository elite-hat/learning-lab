title = 'temperature convertor'
print(title.upper())

print('Enter a temperature')
temp = int(input('Temperature: '))

print('Temperature you entered is: ')
print('1. Celsius')
print('2. Fahrenheit')
print('3. Kelvin')
unit = int(input('> '))

print(f'Convert {temp} in:')
print('1. Celsius')
print('2. Fahrenheit')
print('3. Kelvin')
convertedUnit = int(input('> '))

if unit == 1:
    if convertedUnit == 1:
        print('It is already Celsius')
    elif convertedUnit == 2:
        convertedTemp = ( (9 / 5) * temp) + 32
    elif convertedUnit == 3:
        convertedTemp = temp + 273.15
    else:
        print('Wrong Input')
elif unit == 2:
    if convertedUnit == 1:
        convertedTemp = (temp - 32) * (5 / 9)
    elif convertedUnit == 2:
        print('It is already fahrenheit')
    elif convertedUnit == 3:
        convertedTemp = ((temp - 32) * (5 / 9)) + 273.15
    else:
        print('Wrong Input')
elif unit == 3:
    if convertedUnit == 1:
        convertedTemp = temp - 273.15
    elif convertedUnit == 2:
        convertedTemp = ((temp - 273.15) * (9 / 5)) + 32
    elif convertedUnit == 3:
        print('It is already kelvin')
    else:
        print('Wrong Input')
else:
    print('Wrong Input')
print(convertedTemp)