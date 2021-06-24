# Let's create a class called Sneak

from reptile import Reptile

class Sneak(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True

# Let's add some specific methods/behaviours
    def use_tongue_to_smell(self):
        return "If I can touch it I can smell it "

# Let's create an object of Sneak class
smart_sneak = Sneak()

# print(smart_sneak.move()) # move() is available from Animal class
# print(smart_sneak.hunt()) # hunt() is available from Reptile class
# print(smart_sneak.use_tongue_to_smell()) # from current class

# time to move on to our last step

