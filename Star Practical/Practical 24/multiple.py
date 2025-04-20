class c1:
    def c1_method(self):
        print("This is c1 class method")

class c2():
    def c2_method(self):
        print("This is c2 class method")

class c3(c1,c2):
    def c3_method(self):
        print("This is c3 class method")

m = c3()
m.c1_method()
m.c2_method()
m.c3_method()