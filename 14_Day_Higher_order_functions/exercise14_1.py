import sys
sys.path.append(".")
from data.countries import *
# Exercises: Level 1
# Explain the difference between map, filter, and reduce.

# map: Transforms every item in an iterable using a function
# filter: Selects items that meet a specific condition (True/False)
# reduce: Accumulates all items step-by-step into a single value.

# Explain the difference between higher order function, closure and decorator

#A Higher Order Function is any function that either accepts one or more functions as arguments OR returns a function.
#A Closure occurs when a nested (inner) function remembers and accesses variables from its enclosing (outer) function's scope, even after the outer function has finished executing.
# A Decorator is a design pattern (and a specific syntax in Python using @) that uses both Higher Order Functions and Closures to wrap another function, adding functionality before or after it runs.

# Define a call function before map, filter or reduce, see examples.
def even(num):
    if num %2==0:
        return True
    else:
        return False

names = ["John","Peter",'Austin','Eren']
numbers = [1,1,2,3,4,5,6,7,8,9,10,0]
# Use for loop to print each country in the countries list.
for country in countries:
    print(country)
# Use for to print each name in the names list.
for name in names:
    print(name)
# Use for to print each number in the numbers list.
for number in numbers:
    print(number)