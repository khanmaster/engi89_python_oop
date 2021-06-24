# Python's extensive documentation on python.org
# We have used functions that we created as wel as builtin -

# import is the keyword that is used to import any module available in python.org
# Let's see that in action
# math
import math # to calculate values
from random import random # generates random number

num1 = 23.44 # float

# in real life situation you have to round the figure depending on the value
# if the value is less than .50 round it down 23.0, if 23.51 then round it up

print(math.ceil(num1))
print(math.floor(num1))
print(math.pi)
# Random class/methods
print(random()) #
# generates random number every time the programs is executed between 0.0
# to .99
