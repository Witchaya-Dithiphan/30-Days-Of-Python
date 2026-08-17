# Declare an empty list
l1 = list()
# Declare a list with more than 5 items
l1 = [1,2,3,4,5]
# Find the length of your list
print(len(l1))
# Get the first item, the middle item and the last item of the list
mid = len(l1) // 2
print(l1[0], l1[mid], l1[-1])
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Poom', 20, 175, False, False, "115/1"]
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle' , 'Amazon']
# Print the list using print()
print(mixed_data_types)
print(it_companies)
# Print the number of companies in the list
print(len(it_companies))
# Print the first, middle and last company
mid = len(it_companies) // 2
print(it_companies[0], it_companies[mid], it_companies[-1])
# Print the list after modifying one of the companies
index = it_companies.index("Oracle")
it_companies[index] = "Meta"
print(it_companies)
# Add an IT company to it_companies
it_companies.append("Palantir")
print(it_companies)
# Insert an IT company in the middle of the companies list
it_companies.insert(4,"Tesla")
print(it_companies)
# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)
# Join the it_companies with a string '#;  '
print("#; ".join(it_companies))
# Check if a certain company exists in the it_companies list.
print("Tesla" in it_companies)
# Sort the list using sort() method
l1.sort()
print(l1)
# Reverse the list in descending order using reverse() method
l1.sort(reverse=True)
print(l1)
# Slice out the first 3 companies from the list
print(it_companies[:3])
# Slice out the last 3 companies from the list
print(it_companies[len(it_companies)-3:])
# Slice out the middle IT company or companies from the list
middle = len(it_companies)//2
print(it_companies[middle:middle+1])
# Remove the first IT company from the list
first = it_companies[0]
it_companies.remove(first)
print(it_companies)
# Remove the middle IT company or companies from the list
mid = len(it_companies) // 2
if len(it_companies) % 2 == 0:
    del it_companies[mid-1 : mid+1]  # กรณีคู่ ลบ 2 ตัว
else:
    del it_companies[mid]
# Remove the last IT company from the list
it_companies.pop()
print(it_companies)
# Remove all IT companies from the list
it_companies.clear()
print(it_companies)
# Destroy the IT companies list
del it_companies
# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_end.extend(back_end)
print(front_end)
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end.copy()
index = full_stack.index("Redux")
full_stack[index+1 : index+1] = ['Python', 'SQL']