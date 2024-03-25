class Vehicle:
    def gen_use(self):
        print("Vehicle")
        
class Car(Vehicle):
    def __init__(self):
        self.a=30
        self.b=40
    def sp_use(self):
        print("car")

class motor(Vehicle):
    def __init__(self):
        self.a=90
        self.b=80
    def sp_use(self):
        print("motor")
        
c= Car()
c.gen_use()
c.sp_use()
