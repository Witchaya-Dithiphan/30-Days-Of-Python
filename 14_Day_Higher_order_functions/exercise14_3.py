import sys
sys.path.append(".")
from functools import reduce

from data.countries_data import countries_dict
# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) file and follow the tasks below:
# Sort countries by name, by capital, by population

def sort_countries(pattern,rev = False):
    sort = sorted(countries_dict, key=lambda item: item[f'{pattern}'],reverse = rev)
    return sort
# print(sort_countries("name"))
# print(sort_countries("capital"))
# print(sort_countries("population"))

# Sort out the ten most spoken languages by location.

def most_spoken_languages():
    languages = reduce(lambda acc,country: acc+country['languages'],countries_dict,[])
    count_lang = reduce(lambda acc,language: {**acc,language: acc.get(language,0) + 1}, languages, {})
    sorted_lang = sorted(count_lang.items(), key=lambda item:item[1], reverse=True) 
    return sorted_lang[:10]
print(most_spoken_languages())

# Sort out the ten most populated countries.

def ten_most_population():
    top_ten = sort_countries(pattern = "population",rev = True)[:10]
    top_ten = reduce(lambda acc,country: acc+[(country['name'],country['population'])],top_ten,[])
    return top_ten

print(ten_most_population())