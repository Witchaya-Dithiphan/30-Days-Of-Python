# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    if num <= 1:
        return False
    if num > 2 and num%2==0:
        return False
    for i in range(3,num):
        if num%i==0:
            return False
    return True
print(is_prime(17))
# Write a functions which checks if all items are unique in the list.
def unique(l1):
    return len(set(l1)) == len(l1)
print(unique([1,1,2,3,4,5]))
# Write a function which checks if all the items of the list are of the same data type.
def same_data_type(l1):
    if not l1:
        return True
    first_type = type(l1)
    return all(isinstance(item,first_type) for item in l1)
print(same_data_type([1,2,3,'a']))
# Write a function which check if provided variable is a valid python variable
def is_valid(name):
    return name.isidentifier()
print(is_valid("2_j3k"))
# Go to the data_ folder and access the countries-data.py file.