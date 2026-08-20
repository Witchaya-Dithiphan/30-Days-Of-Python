# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
import re
import json
from functools import reduce

def count_lines_and_words(file_path):
    with open(file_path) as f:
        texts = f.read()
        regex = r'[a-zA-z]+'
        words_count = len(re.findall(regex,texts))
        f.seek(0)
        lines = f.readlines()
        lines_count = len(lines)
        print(f"This paragraph have total {lines_count} lines\nAnd have total {words_count} words")

count_lines_and_words('./data/obama_speech.txt')

# Read michelle_obama_speech.txt file and count number of lines and words
# Read donald_speech.txt file and count number of lines and words
# Read melina_trump_speech.txt file and count number of lines and words

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
def most_spoken_languages(filename,count):
    def top_languages(countries):
        languages = reduce(lambda acc,country: acc+country['languages'],countries,[])
        languages = reduce(lambda acc,language: {**acc, language : acc.get(language,0)+1},languages,{})
        sort_languages = sorted(languages.items(),key = lambda item:item[1],reverse=True)[:count]
        sort_languages = [(count,language) for language,count in sort_languages]
        return sort_languages

    with open(filename, encoding="utf-8") as f:
        countries_dict = json.load(f)
        return top_languages(countries_dict)

print(most_spoken_languages(filename="./data/countries_data.json",count = 3))

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries(filename,count):
    def top_population(countries):
        population = reduce(lambda acc,country: {**acc, country['name'] : country['population']},countries,{})
        sort_population = sorted(population.items(),key = lambda item:item[1],reverse=True)[:count]
        sort_population = [(count,language) for language,count in sort_population]
        return sort_population

    with open(filename, encoding="utf-8") as f:
        countries_dict = json.load(f)
        return top_population(countries_dict)

print(most_populated_countries(filename="./data/countries_data.json",count = 10))