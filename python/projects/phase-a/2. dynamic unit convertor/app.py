from convertor.main import process, display, category_options, unit_options, categories

print("\nDYNAMIC UNIT CONVERTOR")

category_options()
print("\nEnter the category from the above. Write as it is written.")

while True:
    category = input("Category: ")
    if category in categories:
        break
    else:
        print("Invalid Input")

unit_options(category)
while True:
    convert_from = input("\nConvert From: ")
    if convert_from in categories[category]:
        break
    else:
        print("Invalid Input")

print("\nEnter the value to change its unit: ")
while True:
    try:
        value = int(input("Value: "))
        break
    except ValueError:
        print("ValueError")

unit_options(category)
while True:
    convert_to = input("\nConvert To: ")
    if convert_to in categories[category]:
        break
    else:
        print("Invalid Input")

process(category, convert_from, convert_to)

print(display(value))

# Remove any special-case handling for temperature from main logic
# Implement temperature conversion using function-based mappings in the data layer
# Upgrade data structure to support both linear (factor-based) and non-linear (function-based) conversions
# Ensure the convert() function works generically for all categories without branching
# Verify that all conversions strictly follow a unified system (no direct unit-to-unit shortcuts)
# Ensure all unit definitions (including transformations) exist only in data.py
# Confirm that adding a new unit or category requires no changes in logic code
# Make UI dynamically read categories and units from data instead of hardcoding
# Ensure complete separation between UI, logic, and data layers
# Validate inputs thoroughly (invalid category, unit, and value)
# Clean up any remaining hidden hardcoding or conditional logic tied to specific units
# Optionally refine output formatting for consistency and clarity