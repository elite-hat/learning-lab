categories = {
    "length" : {
        "millimeters" : 1000000,
        "meters" : 1000,
        "kilometers" : 1
    },

    "mass" : {
        "milligrams" : 1000000,
        "grams" : 1000,
        "kilograms" : 1
    },

    "time" : {
        "seconds" : 3600,
        "minutes" : 60,
        "hours" : 1
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