from pathlib import Path

# Absolute Path
# Relative Path

path = Path()                     # If we don't add anything in brackets, it will refer to the current directory
for file in path.glob("*"):
    print(file)