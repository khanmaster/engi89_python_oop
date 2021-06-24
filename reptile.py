# Let's create reptile class to inherit Animal class
from animal import Animal # importing Animal class

class Reptile(Animal): # inherting from Animal class

    def __init__(self):
        super().__init__() # super is used to iherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chamber = [3, 4]

    def seek_heat(self):
        return "it's chilly looking have fun in the sun!"

    def hunt(self):
        return "keep working hard to find food "

    def use_venom(self):
        return "If I have it I will use it "

# Let's create an object of Reptile class
smart_reptile = Reptile()
# print(smart_reptile.breathe()) # breathe method is inherited from Animal class
# print(smart_reptile.hunt()) # hunt() is available in Reptile class
# print(smart_reptile.eat())
# print(smart_reptile.move())
# print(smart_reptile.hunt())


