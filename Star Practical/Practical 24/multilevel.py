class c1:
    def c1_method(self):
        print("This is Class c1 method.")

class c2(c1):
    def c2_method(self):
        print("This is Class c2 method.")
        
class c3(c2):
    def c3_method(self):
        print("This is Class c3 method.")

m = c3()
m.c1_method()
m.c2_method()
m.c3_method()