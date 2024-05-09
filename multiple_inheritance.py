class father:
    def skills(self):
        print("Gardening")

class mother:
    def skills(self):
        print("Cooking")

class child(father, mother):
    def skills(self):
        father.skills(self)
        mother.skills(self)
        print("Learning")

c = child()
c.skills()