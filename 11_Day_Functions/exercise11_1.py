# 1 Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a,b):
    return a+b
print(add_two_numbers(2,3))
# 2 Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def circle_area(r):
    pi = 3.14
    return pi * r**2
print(circle_area(2))
# 3 Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(arbitrary):
    try:
        sum = 0
        for num in arbitrary:
            sum+=num
        return sum
    except:
        return "some item in list is not number"
print(add_all_nums([5,2]))
# 4 Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(temperature_C):
    F = (temperature_C * (9/5)) + 32
    return F
print(convert_celsius_to_fahrenheit(25))
# 5 Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_seasons(month):
    Autumn = ['September', 'October' , 'November']
    Winter = ['December', 'January', 'February']
    Spring = [ 'March', 'April' , 'May']
    Summer = ['June', 'July', 'August']
    if month in Autumn:
        return "Autumn"
    elif month in Winter:
        return "Winter"
    elif month in Spring:
        return "Spring"
    elif month in Summer:
        return "Summer"
print(check_seasons("August"))
# 6 Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(point1,point2):
    slope = (point1[1]-point2[1])/(point1[0]-point2[0])
    return slope
print(calculate_slope((0,0),(5,5)))
# 7 Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_equation(a,b,c):
    if a == 0:
        return "a cannot be 0 in quadratic equation"
    d = ((b**2)-(4*a*c))**0.5
    x1 = (-b + d)/2*a
    x2 = (-b - d)/2*a
    return(x1,x2)

    if x1.imag == 0 and x2.imag == 0:
            x1 = x1.real
            x2 = x2.real
    if x1 == x2:
        return (x1,)  # Single solution if discriminant is 0
    return(x1,x2)
    
print(solve_quadratic_equation(1,-5,6))
# 8 Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(l1):
    for item in l1:
        print(item,end=" ")
    print()
print_list([1,2,3,4,5])

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list(["A", "B", "C"])) 
# # ["C", "B", "A"]

def reverse_list(l1):
    return l1[-1::-1]

print(reverse_list([1,2,3,4,5]))

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(l1):
    for i in range(len(l1)):
        l1[i] = l1[i].upper()
    return l1
print(capitalize_list_items(["a","b","c"]))

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))   

def add_item(l1,item):
    l1.append(item)
    return l1
print(add_item([1,2,3,4,5],'apple'))

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
# print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9]
# print(remove_item(numbers, 3))  # [2, 7, 9]

def remove_item(l1,item):
    l1.remove(item)
    return l1
print(remove_item([1,2,3,4,5],5))

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_of_numbers(10)) # 55
# print(sum_of_numbers(100)) # 5050
def sum_of_numbers(num):
    return (num*(num+1))/2
print(sum_of_numbers(154521456145))

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum = 0
    for i in range(1,num+1,2):
        sum+=i
    return sum
print(sum_of_odds(5))

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_evens(num):
    sum = 0
    for i in range(0,num+1,2):
        sum+=i
    return sum
print(sum_of_evens(5))