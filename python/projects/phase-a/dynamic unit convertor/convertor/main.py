categories = {
    "length" : {
        "millimeters" : 1000,
        "meters" : 1,
        "kilometers" : 1 / 1000,
        "inches" : 1 / 40,
        "feet" : 10 / 3,
        "yards" : 0.9144
    },

    "mass" : {
        "milligrams" : 1000000,
        "grams" : 1000,
        "kilograms" : 1,
        "tonnes" : 1 / 1000,
        "pounds" : 2.205
    },

    "time" : {
        "seconds" : 1,
        "minutes" : 1 / 60,
        "hours" : 1 / 3600,
        "days" : 1 / 86400,
        "months" : 1 / 2592000,
        "years" : 1 / 31536000,
        "century" : 1 / 3153600000
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
    global unit
    unit = categ[from_option]
    global convert
    convert = categ[to_option]

def display(value):
    result = (value / unit) * convert
    return (f"\nResult: {result}")