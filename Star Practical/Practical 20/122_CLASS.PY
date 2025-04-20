# Step 1: Creating a class with a method
class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        """Method to add two numbers"""
        return self.num1 + self.num2

# Step 2: Creating an object of the class
calc = Calculator(20, 2)

# Step 3: Accessing method using the object
result = calc.add()

# Printing the result
print(f"The sum of {calc.num1} and {calc.num2} is: {result}")
