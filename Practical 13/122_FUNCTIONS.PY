# Function without argument
def greet():
    print("Hello! Welcome to Python programming.")


# Function with argument
def square(num):
    print(f"Square of {num} is {num * num}")


# Function returning value
def cube(num):
    return num ** 3


# Calling the functions
greet()  # Function without argument

square(5)  # Function with argument

result = cube(3)  # Function returning value
print(f"Cube of 3 is {result}")
