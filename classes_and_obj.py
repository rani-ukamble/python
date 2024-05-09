class Human:
    def __init__(self, n, o):
        self.name = n
        self.occupation = o
        
    def work(self):
        if(self.occupation=="tennis"):
            print(self.name, " plays tennis" )
        elif(self.occupation=="actor"):
            print(self.name, "shoots films" )
            
    def speaks(self):
        print(self.name, ", says how are you?")
        
obj = Human("Tom", "actor")
obj.work()
obj.speaks()