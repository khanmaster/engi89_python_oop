# Python OOP
## Four Pillars of OOP
### Functions and good practice of functions
#### DRY Don't Repeat Yourself

```python
# First Iterations
def greeting():
    print("Welcome on Board! enjoy your trip")
#pass # pass is the keyword that allows the interpreter to skip this without any errors

greeting() # if we didn't call the function it would execute the code with no error but no outcome
# DRY Don't Repeat your self by declaring functions and reusing code
```
- Return statement in a function
```python
# Second Iteration using RETURN statement
def greeting():
    print("Good Morning")
    return "Welcome on board! Enjoy your trip!!"
print(greeting())

```

````python
# Third Iteration with user name as a string as an argument/args

def greeting(name): # name is the arg
#    print(name)
    return "Welcome on Board " + name
print(greeting("James Bond")) # we have to provide 1 arg as a string 

````

```python
# Create a function to prompt the user to enter their name and display the name back to user with greeting message
# 5 min
user_name = input("Please enter your name ")
def greeting(name):
    return "Welcome on Board " + name
    
print(greeting(user_name))

```

```python
# Let's create a function with multiple args as an int

def add(num1, num2):
    return num1 + num2

print(add(9, 3))

# Code after the return statement doesn't get executed as functions exits after the return statement

def multiply(num1, num2):
    print("This functions multiplies 2 numbers ")
    return num1 * num2
    print(" this is the required outcome of 2 numbers ") # this line of code will not execute as return statement is last line of code that function executes
print(multiply(3, 3))

```

#### Python Modules, packages and Lib

- Python's extensive documentation on python.org
- We have used functions that we created as wel as builtin -

- import is the keyword that is used to import any module available in python.org
- Let's see that in action

```python

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
```
```python
# Let's see how can we interact with our machine using python
import os  # os used to get info about your OS
import math, datetime, sys  # sys is used to get system specific information

work_dir = os.getcwd() # getcwd() provides the current location/path
print(work_dir)

# Linux/Mac
# print(os.getuid()) # works on linux and mac
# print(os.uname()) # works on linux and mac
# print(os.cpu_count()) # works on linux and mac

print(datetime.date.today()) # today's date
print(sys.path)
# type() len()

```
- Let's install requests using pip
- `pip install requests`
- To check version ` pip -V `

# Object Oriented Programming (OOP)
## Four Pillars of OOP

- Abstraction 
-
-

- Inheritance
-
-

- encapsulation
- 
-


- Polymorphism
-


- step one create an aimal.py file to create parent class
- step two to create file called reptile.py to abstract data and inherit from animal.py 
- step three is to create a file called snake.py
- step four is to create a file called python.py and this point we should be able to utilise inheritance from multiple classes - everything available from animal class to python

```python
# Let's create an Animal class

class Animal: # follow the correct naming convention
    # we need to initialise with built in method called __init__(self)
    # self refers to current class
    def __init__(self): # we declare attributes in our init method
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        return "Keep breathing to stay alive !"

    def eat(self):
        return "time to eat "

    def move(self):
        return "move left and right to stay awake "

# we need to create an object of this class in order to use any methods
cat = Animal() # creating an object of Animal class
# for cat as a user the functionality inside Animal class and the method breathe is abstracted
# print(cat.breathe())
# print(cat.eat())

# Let's move onto our step 2
```
```python
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

```
```python


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

```
```python
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
```