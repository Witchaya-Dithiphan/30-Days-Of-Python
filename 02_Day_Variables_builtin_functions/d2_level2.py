#Day 2: 30 Days of python programming
first_name = 'Witchaya'
last_name = "Dithiphan"
full_name = "Witchaya Dithiphan"
country = "Thailand"
city = "Pattaya"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = False 
Nickname , university = "Poom" , "KMITL"

print(type(first_name)) # <class 'str'>
print(type(last_name)) # <class 'str'>
print(type(full_name)) # <class 'str'>
print(type(country)) # <class 'str'>
print(type(city)) # <class 'str'>
print(type(age)) # <class 'int'>
print(type(year)) # <class 'int'>
print(type(is_married)) # <class 'bool'>
print(type(is_true)) # <class 'bool'>
print(type(is_light_on)) # <class 'bool'>
print(type(Nickname)) # <class 'str'>
print(type(university)) # <class 'str'>

print(len(first_name)) # 8
print(len(last_name)) # 8
print(len(first_name) == len(last_name)) # True

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

print(total) # 9
print(diff) # 1 
print(product) # 20
print(division) # 1.25
print(remainder) # 4
print(exp) # 625
print(floor_division) # 1

radius = 30
area_of_circle = 3.14 * radius ** 2
print(area_of_circle) # 2826.0
circum_of_circle = 2 * 3.14 * radius
print(circum_of_circle) # 188.4
radius = float(input("Enter radius: "))
print("Area of circle: ", 3.14 * radius ** 2)

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))
print("Your first name is: ", first_name)
print("Your last name is: ", last_name)
print("You are from: ", country)
print("You are ", age, " years old.")