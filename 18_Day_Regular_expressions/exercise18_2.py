# # Write a pattern which identifies if a string is a valid python variable

# is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True

import re

name = input("Enter your name: ")
def is_valid_variable(name):
    regex = r'[A-Za-z]+_[A-Za-z]+|[A-Za-z]+'
    find = re.match(regex,name)
    if find != None and find.span()[1] == len(name):
        return True
    else:
        return False

print(is_valid_variable(name))