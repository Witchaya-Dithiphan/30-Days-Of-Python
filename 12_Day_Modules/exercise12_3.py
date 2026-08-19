from random import shuffle , randint , choice
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list

def shuffle_list(l1):
    shuffled = l1.copy()
    shuffle(shuffled)
    return shuffled

print(shuffle_list([1,2,3,4,5]))

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.

def unique_num():
    unique = []
    while len(unique) < 7:
        num = randint(0,9)
        if num not in unique:
            unique.append(num)
    return unique

print(unique_num())