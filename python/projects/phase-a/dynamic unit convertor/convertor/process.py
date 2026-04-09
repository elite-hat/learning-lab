from app import operation
import length, weight, temperature

results = {
    [1, 1] : length.meters_to_yards,
    [1, 2] : length.yards_to_meters,
    [2, 1] : weight.kilograms_to_pounds,
    [2, 2] : weight.pounds_to_kilograms,
    [3, 1] : temperature.centigrade_to_fahrenheit,
    [3, 2] : temperature.fahrenheit_to_centigrade
}