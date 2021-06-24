# Let's create python class

from sneak import Sneak

class Python(Sneak):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True


    def digest_large_prey(self):
        return "I can digest anything without chewing "

    def climb(self):
        return "up we go....."

    def __shed_skin(self):
        return "I'm growing out of my skin now "

fast_python = Python()
print(fast_python.__)






# print(fast_python.climb())
# print(fast_python.hunt())
# print(fast_python.move())
# print(fast_python.use_tongue_to_smell())
# print(fast_python.shed_skin())