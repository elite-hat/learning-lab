def centigrade_to_fahrenheit(centigrade):
    fahrenheit = centigrade * 9 / 5 + 32
    return fahrenheit

def fahrenheit_to_centigrade(fahrenheit):
    centigrade = (fahrenheit - 32) * (5 / 9)
    return centigrade

print(fahrenheit_to_centigrade(212))