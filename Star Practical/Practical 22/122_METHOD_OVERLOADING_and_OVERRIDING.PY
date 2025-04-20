class Parent:
    def show(self):
        print("This is the Parent class method.")

class Child(Parent):
    def show(self):  # Method Overriding
        print("This is the Child class method (Overridden).")

class Calculator:
    def add(self, a=None, b=None, c=None):  # Method Overloading (Simulated)
        if a is not None and b is not None and c is not None:
            return a + b + c
        elif a is not None and b is not None:
            return a + b
        else:
            return "Provide at least two numbers!"

# Method Overriding
p = Parent()
c = Child()

print("Method Overriding Example:")
p.show()  # Calls Parent class method
c.show()  # Calls overridden method in Child class

print("\nMethod Overloading Example:")
calc = Calculator()
print("Addition of 2 numbers:", calc.add(5, 10))  # Two arguments
print("Addition of 3 numbers:", calc.add(3, 7, 2))  # Three arguments
print("Invalid case:", calc.add(5))  # One argument (Error case)
