# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
sum = 0
for i in range(101):
    sum+=i
print(sum)
# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.
sum = 0
for i in range(0,101,2):
    sum+=i
print(sum)