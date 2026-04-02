# MODULES

# NOTE: Modules is to write code in multiple files, to organize our code.

# Method 1
import convertors
print(convertors.kg_to_lbs(70))

# Method 2
from convertors import kg_to_lbs
print(kg_to_lbs(70))

# Summary
'''
1. We use modules to better organize our code
2. We breakup our code in different files
3. Each file is called a module, and it usually contains functions or classes
4. There are two methods to import a module
'''