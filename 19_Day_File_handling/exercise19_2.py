import re
from functools import reduce
from collections import Counter
import sys; sys.path.append(".")
from data.stop_words import *

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

with open("./data/email_exchanges_big.txt") as f:
    text = f.read()
    regex = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    email_count = re.findall(regex,text)
    print(email_count)

# Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. Check the output
#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 10))
#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and'),
#     (4, 'a'),
#     (4, 'in'),
#     (3, 'that'),
#     (2, 'have'),
#     (2, 'I')]

#     # Your output should look like this
#     print(find_most_common_words('sample.txt', 5))

#     [(10, 'the'),
#     (8, 'be'),
#     (6, 'to'),
#     (6, 'of'),
#     (5, 'and')]
def find_most_common_words(filename,count):
    with open("./data/donald_speech.txt") as f:
        text = f.read()
        regex = r'[A-Za-z]+'
        words = re.findall(regex,text)
        words_count = reduce(lambda acc,word: {**acc, word:acc.get(word,0)+1},words,{})
        sort_count = sorted(words_count.items(),key=lambda item:item[1],reverse = True)[:count]
        sort_count = [(count,word) for word, count in sort_count]
        return sort_count
print(find_most_common_words('./data/donald_speech.txt', count = 5))

# Use the function, find_most_frequent_words to find:
# The ten most frequent words used in Obama's speech
# The ten most frequent words used in Michelle's speech
# The ten most frequent words used in Trump's speech
# The ten most frequent words used in Melina's speech

def find_most_common_words2(filename,count):
    with open("./data/donald_speech.txt") as f:
        text = f.read()
        regex = r'[A-Za-z]+'
        words = re.findall(regex,text)
        words_count = Counter(
                    word
                    for word in words
                )
        words_count = [(count,word) for word, count in words_count.most_common(10)]
        return words_count
print(find_most_common_words2('./data/melina_speech.txt', count = 10))
# Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words are in the data directory

f1 = open("./data/melina_trump_speech.txt")
f2 = open("./data/michelle_obama_speech.txt")

melina = f1.read()
michelle = f2.read()
f1.close()
f2.close()

def clean_text(text):
    pattern = r'[A-Za-z\']+'
    text = set(re.findall(pattern,text))
    return text

def remove_support_words(text,stop_words = stop_words):
    stop_words = set(stop_words)
    text.difference(stop_words)
    return text

def check_text_similarity(text1,text2):
    same_words = text1.intersection(text2)
    all_words = text1.union(text2)
    similarity = len(same_words)/len(all_words)
    return similarity

melina = clean_text(melina)
michelle = clean_text(michelle)

melina = remove_support_words(text = melina,stop_words= stop_words)
michelle = remove_support_words(text = michelle,stop_words= stop_words)

print("Similarity is: ",check_text_similarity(melina,michelle))

# Read the hacker news csv file and find out:

import csv
with open("./data/hacker_news.csv") as f:
    csv_reader = csv.reader(f, delimiter=',')
    python = 0
    jvs=0
    java=0

    for row in csv_reader:
        for col in row:
            if re.search(r'[Pp]ython',col) != None:
                python+=1
            if re.search(r'[Jj]ava[Ss]cript',col)!=None:
                jvs+=1
            if re.search(r'[Jj]ava$',col)!=None:
                java+=1
    print("Python: ",python)
    print("JavaScript: ",jvs)
    print("Java: ",java)


# Count the number of lines containing python or Python
# Count the number lines containing JavaScript, javascript or Javascript
# Count the number lines containing Java and not JavaScript