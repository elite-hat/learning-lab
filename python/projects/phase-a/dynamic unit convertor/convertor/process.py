from convertor import length, weight, temperature

def convert(n, a, b):
    options = {
        1 : {
            1 : length.meters_to_yards(n),
            2 : length.yards_to_meters(n)
        },
        2 : {
            1 : weight.kilograms_to_pounds(n),
            2 : weight.kilograms_to_pounds(n)
        },
        3 : {
            1 : temperature.centigrade_to_fahrenheit(n),
            2 : temperature.fahrenheit_to_centigrade(n)
        }
    }

    return options[a][b]