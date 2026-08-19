import sys; sys.path.append(".")  # Adds current terminal workspace root
from data.countries import countries
from data.countries_data import countries_dict
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
for country in countries:
    if "land" in country:
        print(country)
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
fruits = ['banana', 'orange', 'mango', 'lemon']
rev_fruits = []
for fruit in fruits:
    rev_fruits.insert(0,fruit)
print(rev_fruits)
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
languages = []
for country in countries_dict:
    for language in country['languages']:
        languages.append(language)
print(len(set(languages)))
# Find the ten most spoken languages from the data
count_lang = {}
for language in languages:
    count_lang[f'{language}'] = count_lang.get(language,0)+1
sorted_lan = dict(sorted(count_lang.items(), key=lambda item: item[1], reverse=True))

top10_languages = list(sorted_lan.items())[:10]
for item in top10_languages:
    print(f"{item[0]} : {item[1]}")
# Find the 10 most populated countries in the world

sorted_pop = sorted(countries_dict, key=lambda item: item['population'], reverse=True)
top10_population = sorted_pop[:10]

for item in top10_population:
    print(f"{item['name']} : {item['population']}")
