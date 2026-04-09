def length():
    options = ["meters to yards", "yards to meters"]
    return options

def weight():
    options = ["kilograms to pounds", "pounds to kilograms"]
    return options

def temperature():
    options = ["centigrade to fahrenheit", "fahrenheit to centigrade"]
    return options

categories = {
    1 : length(),
    2 : weight(),
    3 : temperature()
}

def display(option_category):
    print("OPTIONS:")
    i = 0
    for option in categories[option_category]:
        i += 1
        print(f"{i}. {option}")