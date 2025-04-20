class MyClass:
    def greet(self, name=None):
        if name:
            print("Hello,", name)
        else:
            print("Hello!")

obj = MyClass()
obj.greet()            # Hello!
obj.greet("Sahil")     # Hello, Sahil
