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