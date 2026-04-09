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

def display():
    sr = 0
    for i in categories:
        category = categories[i]
        for j in category:
            sr += 1
            print(f"{sr}. {category[j]}")