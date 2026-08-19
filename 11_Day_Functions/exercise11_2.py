# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

def evens_and_odds(num):
    if num % 2 ==0:
        return f"The number of odds are {(num//2)}\nThe number of evens are {(num//2)+1}"
    else:
        return f"The number of odds are {(num//2)+1}\nThe number of evens are {(num//2)+1}"
print(evens_and_odds(1000001))
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(i):
    if i == 1:
        return 1
    return i * factorial(i-1)
print(factorial(3))
# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(box):
    if len(box) == 0:
        return True
    else:
        return False
print(is_empty([]))
# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
l1 = [1,4,2,3,6,8,2,4,6,8,4,2,1,3,3,5,4,4,6,9,8,7,1,2,3,6,5,4,7,8,9]

def calculate_mean(l1):
    mean = sum(l1)/len(l1)
    return mean
print(calculate_mean(l1))

def calculate_median(l1):
    l1.sort()
    mid = len(l1)//2
    if len(l1) %2 ==0:
        median = l1[mid-1:mid+1].sum
    else:
        median = l1[mid]
    return median
print(calculate_median(l1))

def calculate_mode(l1):
    l1_mode = {}
    for item in l1:
        l1_mode[item] = l1_mode.get(item,0) + 1
    mode = sorted(l1_mode.items(),key=lambda item:item[1], reverse = True)
    max = mode[0]
    return max
print(calculate_mode(l1))

def calculate_range(l1):
    range = max(l1)-min(l1)
    return range 
print(calculate_range(l1))

def calculate_variance(l1):
    mean = calculate_mean(l1)
    sigma = 0
    for i in l1:
        sigma += (i - mean)**2
    v = sigma/len(l1)
    return v
print(calculate_variance(l1))

def calculate_std(l1):
    v = calculate_variance(l1)
    std = v**0.5
    return std
print(calculate_std(l1))
# Write a function called greet which takes a default argument, name. If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.
#     greet()
#     # "Hello, Guest!
#     greet("Alice")
#     "Hello, Alice!"

def greet(name="Guest"):
    print(f"Hello, {name}!")
greet("Poom")
greet()

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values.
# show_args(name="Alice", age=30, city="New York")
# # Received: name: Alice, age: 30, city: New York
# show_args(name="Bob", pet="Fluffy, the bunny")
# # Received: name: Bob, pet: Fluffy, the bunny

def show_args(**kwargs):
    # Format each key-value pair as "key: value"
    formatted_args = [f"{key}: {value}" for key, value in kwargs.items()]
    
    # Join them together with comma and space
    output_string = ", ".join(formatted_args)
    
    # Print in the requested format
    print(f"# Received: {output_string}")


# Example 1:
show_args(name="Alice", age=30, city="New York")
# Output: # Received: name: Alice, age: 30, city: New York

# Example 2:
show_args(name="Bob", pet="Fluffy, the bunny")
# Output: # Received: name: Bob, pet: Fluffy, the bunny