# 1. Function with positional/required arguments
def add_numbers(a, b):
    """Adds two required arguments"""
    return a + b

# 2. Function with keyword arguments
def greet(name, message):
    """Uses keyword arguments"""
    return f"{message}, {name}!"

# 3. Function with default arguments
def power(base, exponent=2):
    """Calculates the power with a default exponent of 2"""
    return base ** exponent

# 4. Function with variable-length arguments (*args)
def sum_all(*numbers):
    """Sums up all numbers given as arguments"""
    return sum(numbers)

# Testing the functions
print(add_numbers(5, 10))              # Positional argument
print(greet(name="Sahil", message="Hello"))  # Keyword argument
print(power(4))                        # Default argument
print(power(3, 3))                     # Overriding default argument
print(sum_all(1, 2, 3, 4, 5))          # Variable length argument
