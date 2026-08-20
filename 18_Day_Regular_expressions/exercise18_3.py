import re
from functools import reduce

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

regex = r'[^A-Za-z ]'
clean_sentence = re.sub(regex,"",sentence)
print(clean_sentence)

def counting_words(paragraph):
    words = re.findall(r'[A-za-z]+',paragraph)
    count_words = reduce(lambda acc,word: {**acc,word : acc.get(word,0)+1},words,{})
    return count_words

words = counting_words(clean_sentence)
sort_words = sorted(words.items(),key=lambda item: item[1],reverse=True)
print(sort_words[:3])