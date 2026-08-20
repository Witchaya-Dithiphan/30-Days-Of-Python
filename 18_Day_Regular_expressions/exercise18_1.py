# What is the most frequent word in the following paragraph?
import re
from functools import reduce

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

def counting_words(paragraph):
    words = re.findall(r'[A-za-z]+',paragraph)
    count_words = reduce(lambda acc,word: {**acc,word : acc.get(word,0)+1},words,{})
    return count_words

words = counting_words(paragraph)
sort_words = sorted(words.items(),key=lambda item: item[1],reverse=True)
maximum = sort_words[0]
print(maximum)

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.

text = "the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
points = re.findall(r'-?\d+',text)
points = list(map(lambda point: int(point),points))
rang = max(points) - min(points)
print(rang)