# 1. Write a code which gives grade to students according to theirs scores:
# ```sh
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
# ```

score = int(input("Enter your score: "))
if score >= 90 and score <= 100:
    print("Your grade is A.")
elif score >= 80 and score <= 89:
    print("Your grade is B.")
elif score >= 70 and score <= 79:
    print("Your grade is C.")
elif score >= 60 and score <= 69:
    print("Your grade is D.")
elif score >= 0 and score <= 59:
    print("Your grade is F.")

# 2. Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer

month = input("Enter your birth month: ")
Autumn = ['September', 'October' , 'November']
Winter = ['December', 'January', 'February']
Spring = [ 'March', 'April' , 'May']
Summer = ['June', 'July', 'August']
if month in Autumn:
    print("the season is Autumn")
elif month in Winter:
    print("the season is Winter")
elif month in Spring:
    print("the season is Spring")
elif month in Summer:
    print("the season is Summer")

# 3. The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruit = input("Enter your fruit: ")
if fruit in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit)
    print(fruits)