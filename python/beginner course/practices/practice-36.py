from pathlib import Path

my_path = Path()
for file in my_path.glob("*"):
    print(file)

# !Alternatives:

#   "*"
#   "*.*"
#   "*.txt"
#   "README.*"