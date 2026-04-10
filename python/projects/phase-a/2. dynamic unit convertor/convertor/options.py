length_options = {
    1 : "meters to yards",
    2 : "yards to meters"
}

weight_options = {
    1 : "kilograms to pounds",
    2 : "pounds to kilograms"
}

temperature_options = {
    1 : "centigrade to fahrenheit",
    2 : "fahrenheit to centigrade"
}

categories = {
    1 : length_options,
    2 : weight_options,
    3 : temperature_options
}

units = {
    1 : "meters",
    2 : "yards",
    3 : "kilograms",
    4 : "pounds",
    5 : "centigrade",
    6 : "fahrenheit"
}

def display(category_id):
    global sr
    sr = 0
    category = categories[category_id]
    for j in category:
        sr += 1
        print(f"{sr}. {category[j]}")

def number_of_options():
    return sr