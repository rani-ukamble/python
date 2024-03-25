class Human:
    def __init__(self, n, o):
        self.name=n
        self.occu=o
    def work(self):
        if self.occu=="tennis player":
            print(self.name, " plays tennis")
        else:
            print("another")
            

    
            
            
tom= Human("Raj", "tennis player")
print(tom.work())