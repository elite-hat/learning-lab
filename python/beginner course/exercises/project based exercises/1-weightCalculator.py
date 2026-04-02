# WEIGHT CALCULATOR

weight = input("Weight: ")
unit = input("(L)bs or (K)g: ")

weight = int(weight)

if unit == "L" or unit == "l":
    result = weight * 0.45
    unit = "kilos"
elif unit == "K" or unit == "k":
    result = weight / 0.45
    unit = "pounds"

result = float(result)

print(f"Your are {result:2} {unit}")