# when projects grow, you can not keep everything in one file.
# Modules help you structure code properly

# A module is a python file that contains functions , classes , or variables

# example:
# file: calculator.py

def subtract(a,b):
    return a - b

# now another file can  import this module and use it.


# Types of Modules:
# 1. Built in  Modules:  imported by python itself. import math, import random,import datetime
#2. User defined Modules:  created by users. like calculator.py
# 3. External Modules: created by third party developers. like numpy, pandas, matplotlib, etc.

# different ways to import modules:

# methid 1  - Full import
'''
import calculator
result = calculator.subtract(10,5)
print(result)
'''
# safer , clear namespace 

# method 2 - selective import
'''
from calculator import add
print(add(10,5))
'''
# cleaner but may cause naming conflicts in large projects

# method 3 - aliasing
'''import calculator as cal
print(cal.subtract(10,5))'''
# shorter name but may reduce readability

# The __name__ variable in a module is a special built in variable that holds the name of the module.

print(__name__) # when run directly, it will print __main__

# if you import it 
# import calculator
# print(calculator.__name__) # it will print calculator

# if __name__ == "__main__":

def add (a,b):
    return a + b

if __name__ == "__main__":
    print("Running calculator module directly")
    print(add(3,4))
    