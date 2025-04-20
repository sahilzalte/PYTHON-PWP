# Demonstrating Constructors in Python

class Demo:
    # 1. Default Constructor
    def __init__(self):
        print("Default Constructor Called - No parameters")

# 2. Parameterized Constructor
class ParameterizedDemo:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print(f"Parameterized Constructor Called - Values: a = {self.a}, b = {self.b}")

# 3. Constructor Overloading (Simulated using *args)
class OverloadedDemo:
    def __init__(self, *args):
        if len(args) == 0:
            print("Overloaded Constructor: No arguments provided (Default Constructor)")
        elif len(args) == 1:
            self.a = args[0]
            print(f"Overloaded Constructor: One argument provided - a = {self.a}")
        elif len(args) == 2:
            self.a = args[0]
            self.b = args[1]
            print(f"Overloaded Constructor: Two arguments provided - a = {self.a}, b = {self.b}")
        else:
            print("Overloaded Constructor: Too many arguments provided")

# Creating Objects
print("\n1. Default Constructor")
obj1 = Demo()

print("\n2. Parameterized Constructor")
obj2 = ParameterizedDemo(10, 20)

print("\n3. Constructor Overloading")
obj3 = OverloadedDemo()          # No arguments
obj4 = OverloadedDemo(5)         # One argument
obj5 = OverloadedDemo(3, 7)      # Two arguments
