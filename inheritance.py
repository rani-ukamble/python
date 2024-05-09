class vehicle:
    def uses(self):
        print("Transportation")
        
class car(vehicle):
    def __init__(self):
        print("car")
        self.wheels=4
        self.roof=True
    def spUses(self):
        print("Vaccation")
        
class bike(vehicle):
    def __init__(self):
        print("bike")
        self.wheels=2
        self.roof=False
        
c = car() #constructor called
c.uses()
c.spUses()


# isinstance and issubclass

b = bike()
print(isinstance(b, bike))
print(issubclass(car, vehicle))
           