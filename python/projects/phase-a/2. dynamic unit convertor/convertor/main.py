categories = {
    "length" : {
        "millimeters" : (1000, 0),
        "meters" : (1, 0),
        "kilometers" : (1 / 1000, 0),
        "inches" : (40, 0),
        "feet" : (10 / 3, 0),
        "yards" : (0.9144, 0)
    },

    "mass" : {
        "milligrams" : (1000000, 0),
        "grams" : (1000, 0),
        "kilograms" : (1, 0),
        "tonnes" : (1 / 1000, 0),
        "pounds" : (2.205, 0)
    },

    "time" : {
        "seconds" : (1, 0),
        "minutes" : (1 / 60, 0),
        "hours" : (1 / 3600, 0),
        "days" : (1 / 86400, 0),
        "months" : (1 / 2592000, 0),
        "years" : (1 / 31536000, 0),
        "century" : (1 / 3153600000, 0)
    },

    "temperature" : {
        "celsius" : (1, 0),
        "fahrenheit" : (5/9, 32),
        "kelvin" : (1, -273.15)
    }
}

def category_options():
    i = 0
    for category in categories:
        i += 1
        print(f"- {category}")

def unit_options(category):
    i = 0
    print("\n")
    for option in categories[category]:
        i += 1
        print(f"- {option}")

def process(category, from_option, to_option):
    categ = categories[category]
    global unit_factor, unit_offset
    unit_factor, unit_offset = categ[from_option]
    global convert_factor, convert_offset
    convert_factor, convert_offset = categ[to_option]

def display(value):
    base_value = (value - unit_offset) / unit_factor
    result = base_value * convert_factor + convert_offset
    return (f"\nResult: {result}")