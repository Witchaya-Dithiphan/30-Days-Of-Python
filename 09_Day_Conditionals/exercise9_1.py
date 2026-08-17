# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.

user_age = int(input("Enter your age: "))
if user_age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {18-user_age} more years to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

# Enter your age: 30
# You are 5 years older than me.
my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))

if my_age > your_age:
    diff = my_age-your_age
    year_str = "years" if diff > 1 else "year"
    print(f"You are {diff} {year_str} younger than me.")
elif your_age > my_age:
    diff = your_age-my_age
    year_str = "years" if diff > 1 else "year"
    print(f"You are {your_age-my_age} {year_str} older than me.")
else:
    print("We are the same age")

# 3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = int(input("Enter number one: "))
b = int(input("Enter number two: "))

if a > b:
    print(f"{a} is greater than {b}")
elif b > a:
    print(f"{a} is smaller than {b}")
else:
    print("a is equal to b")