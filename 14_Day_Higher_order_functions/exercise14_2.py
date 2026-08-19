from exercise14_1 import *
from functools import reduce
import sys
sys.path.append(".")
# Use map to create a new list by changing each country to uppercase in the countries list

countries_upper = list(map(lambda name: name.upper(),countries))
print(countries_upper)

# Use map to create a new list by changing each number to its square in the numbers list

square_number = list(map(lambda num:num**2,numbers))
print(square_number)

# Use map to change each name to uppercase in the names list

names_upper = list(map(lambda name: name.upper(),names))
print(names_upper)

# Use filter to filter out countries containing 'land'.

not_land_country = list(filter(lambda name : "land" not in name,countries))
print(not_land_country)

# Use filter to filter out countries having exactly six characters.

not_len_6 = list(filter(lambda name: len(name) != 6,countries))
print(not_len_6)

# Use filter to filter out countries containing six letters and more in the country list.

above_len_6 = list(filter(lambda name: len(name) < 6, countries))
print(above_len_6)

# Use filter to filter out countries starting with an 'E'

not_start_with_E = list(filter(lambda name: name[0] != 'E',countries))
print(not_start_with_E)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))

sum_of_even_cube = reduce(lambda n,m:n+m , map(lambda n:n**3,filter(lambda n:n%2==0,numbers)))
print(sum_of_even_cube)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def get_string_lists(l1):
    return list(map(lambda n:str(n),l1))
print(get_string_lists(numbers))

# Use reduce to sum all the numbers in the numbers list.

sum = reduce(lambda a,b:a+b,numbers)
print(sum)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries

nordic = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
nordic = reduce(lambda a,b:f"{a}, {b}" if b != 'Iceland' else f"{a} and {b}",nordic) + ' are north European countries'
print(nordic)

# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).

def categorize_countries(pattern):
    return list(filter(lambda country: pattern.lower() in country.lower(),countries))
print(categorize_countries("land"))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.

def start_letter(countries):
    start = list(map(lambda country : country[0],countries))
    count_start = reduce(
        lambda acc, letter: {**acc, letter: acc.get(letter, 0) + 1}, 
        start, 
        {}  # ค่าเริ่มต้นของ acc
    )
    return count_start
print(start_letter(countries))

# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.

def get_first_n_countries(n=10):
    return countries[:n]

first_ten_countries = get_first_n_countries(10)

print(first_ten_countries)

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.

def get_last_n_countries(n=10):
    return countries[-1:-1-n:-1]

last_ten_countries = get_last_n_countries(10)

print(last_ten_countries)