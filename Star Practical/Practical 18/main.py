# main.py

# Importing the custom package
# import mypackage

from mypackage import math_operations as mypackage
# Using functions from the package
num1 = 10
num2 = 5

print(f"Addition: {mypackage.add(num1, num2)}")
print(f"Subtraction: {mypackage.subtract(num1, num2)}")
print(f"Multiplication: {mypackage.multiply(num1, num2)}")
print(f"Division: {mypackage.divide(num1, num2)}")
