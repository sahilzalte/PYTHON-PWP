class c1:
    def c1_method(self):
        print("This is c1 class method")
        
class c2(c1):
    def c2_method(self):
        print("This is c2 class method")
        
        
m = c2()
m.c1_method()
m.c2_method()
