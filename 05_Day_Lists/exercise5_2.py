import sys; sys.path.append(".")  # Adds current terminal workspace root

from data.countries import countries
from data.countries import countries
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# Sort the list and find the min and max age
ages.sort()
print(ages)
print(min(ages))
print(max(ages))
# Add the min age and the max age again to the list
ages.extend([min(ages),max(ages)])
print(ages)
# Find the median age (one middle item or two middle items divided by two)
ages.sort()
mid = len(ages)//2
if len(ages) %2 == 1:
    med = ages[mid]
else:
    med = sum(ages[mid-1:mid+1])/2
print(med)
# Find the average age (sum of all items divided by their number )
mean = sum(ages)/len(ages)
print(mean)
# Find the range of the ages (max minus min)
rang = max(ages) - min(ages)
print(rang)
# Compare the value of (min - average) and (max - average), use abs() method
min_age = min(ages)
max_age = max(ages)
rang_min = abs(min_age-mean)
rang_max = abs(max_age - mean)
print(rang_min < rang_max , rang_min == rang_max , rang_min > rang_max)
# Find the middle country(ies) in the countries list
mid = len(countries)//2
if len(countries)%2 == 1:
    print(countries[mid])
else:
    print(countries[mid-1:mid+1])
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if len(countries)%2 == 1:
    l1 = countries[:mid+1]
    l2 = countries[mid+1:]
else:
    l1 = countries[:mid]
    l2 = countries[mid:]
    
# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first , second , third , *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(first)
print(second)
print(third)
print(scandic_countries)