# DICTIONARIES

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
print(customer["name"])
print(customer.get("birthdate"))    # It doesn't exist in dictionary, but using .get allows us to use it wihtout giving an error.
print(customer.get("birthdate", "Jan 1, 1980"))
customer["name"] = "Jack Smith"
print(customer["name"])
customer["birthdate"] = "Jan 1 1980"