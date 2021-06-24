# Python's extensive documentation on python.org
# We have used functions that we created as wel as builtin -

# import is the keyword that is used to import any module available in python.org
# Let's see that in action
# math
# import math # to calculate values
# from random import random # generates random number
#
# num1 = 23.44 # float
#
# # in real life situation you have to round the figure depending on the value
# # if the value is less than .50 round it down 23.0, if 23.51 then round it up
#
# print(math.ceil(num1))
# print(math.floor(num1))
# print(math.pi)
# # Random class/methods
# print(random()) #
# # generates random number every time the programs is executed between 0.0
# # to .99

# Let's see how can we interact with our machine using python
# import os  # os used to get info about your OS
# import math, datetime, sys  # sys is used to get system specific information
#
# work_dir = os.getcwd() # getcwd() provides the current location/path
# print(work_dir)
#
# # Linux/Mac
# # print(os.getuid()) # works on linux and mac
# # print(os.uname()) # works on linux and mac
# # print(os.cpu_count()) # works on linux and mac
#
# print(datetime.date.today()) # today's date
# print(sys.path)
# type() len()

# we can make an API call to any web address using python requests packages
# pip is a package manager in python to install any packages
# pip install requests -
# pip -v

import requests

requests_api = requests.get("https://www.bbc.co.uk/")

if requests_api.status_code == 200: # True
    print("success")
# print(type(requests_api.status_code)) # 200 for success - 404 and above for failure
# print(type(requests_api.headers))
# print(type(requests_api.content))








