# ### Exercises: Level 3
ages_lt = [22, 19, 24, 25, 26, 24, 25, 24]
# 1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?
ages_st = set(ages_lt)
print(len(ages_lt))
print(len(ages_st))
# 2. Explain the difference between the following data types: string, list, tuple and set
# String: a sequence of characters. Immutable.
# List: An ordered, mutable collection that allows duplicate items.
# Tuple: An ordered, immutable collection that allows duplicate items.
# Set: An unordered collection of unique items with no duplicate members.
# 3. _I am a teacher and I love to inspire and teach people._ How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
text = "I am a teacher and I love to inspire and teach people.".split(" ")
unique = set(text)
print(len(unique))