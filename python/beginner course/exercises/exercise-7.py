# If name is less than 3 characters
#   name should be at least  characters
# otherwise if it more than 50 characters
#   name can be maximum of 50 characters
# otherwise
#   name looks good!

name = input()

if len(name) < 3:
    print("name should be at least 3 characters")
elif len(name) > 50:
    print("name can be maximum of 50 characters")
else:
    print("name looks good!")

# SOLUTION

# name = "j"
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name must be maximum of 50 characters")
else:
    print("name looks good!")