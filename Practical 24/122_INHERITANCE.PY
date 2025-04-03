# 1. Single Inheritance
class Parent:
    def parent_method(self):
        print("This is the Parent class method.")

class Child(Parent):
    def child_method(self):
        print("This is the Child class method.")

print("1. Single Inheritance")
obj1 = Child()
obj1.parent_method()  # Accessing Parent class method
obj1.child_method()   # Accessing Child class method

print("\n---------------------------------\n")

# 2. Multiple Inheritance
class ClassA:
    def method_a(self):
        print("This is ClassA method.")

class ClassB:
    def method_b(self):
        print("This is ClassB method.")

class MultipleInheritance(ClassA, ClassB):
    def method_c(self):
        print("This is MultipleInheritance class method.")

print("2. Multiple Inheritance")
obj2 = MultipleInheritance()
obj2.method_a()  # From ClassA
obj2.method_b()  # From ClassB
obj2.method_c()  # Own method

print("\n---------------------------------\n")

# 3. Multilevel Inheritance
class GrandParent:
    def grandparent_method(self):
        print("This is the GrandParent class method.")

class Parent(GrandParent):
    def parent_method(self):
        print("This is the Parent class method.")

class Child(Parent):
    def child_method(self):
        print("This is the Child class method.")

print("3. Multilevel Inheritance")
obj3 = Child()
obj3.grandparent_method()  # From GrandParent class
obj3.parent_method()       # From Parent class
obj3.child_method()        # Own method
