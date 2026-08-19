# Filter only negative and zero in the list using list comprehension
import math
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_evens = [i for i in numbers if i < 0 and i % 2 == 0]
print(negative_evens)

# Flatten the following list of lists of lists to a one dimensional list :

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flatten_list = [number for rows in list_of_lists for number in rows]
print(flatten_list)

# output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Using list comprehension create the following list of tuples:

# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

list_of_tuple = [(i, *(i**n for n in range(6))) for i in range(11)]
print(list_of_tuple)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

countries = [country[0] for country in countries]
flatten_countries = [[country[0].upper(),country[0][0:3].upper(),country[1].upper()] for country in countries]
print(flatten_countries)
# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

countries_dict = [{'country':country.upper(),'city':city.upper()} for [(country,city)] in countries] 
print(countries_dict)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
list_of_concatenated_string = [f"{first_name} {last_name}" for [(first_name,last_name)] in names]
print(list_of_concatenated_string)
# Write a lambda function which can solve a slope or y-intercept of linear functions.

slope = lambda x1,y1,x2,y2: (y1-y2)/(x1-x2)
print(slope(1,1,5,9))