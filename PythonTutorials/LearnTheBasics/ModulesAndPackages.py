__author__ = 'Jitter'

import re

# Your code goes here
module_function_list = dir(re)
find_functions = []

for x in module_function_list:
    if x.find("find") != -1: #more elegant: if find in x
        find_functions.append(x)

print(find_functions)
