class a :
    def method(self, name = None):
        if name:
            print("hello world",name)
        else:
            print("hello world")
        
obj = a()
# obj.method()
obj.method("sahil")