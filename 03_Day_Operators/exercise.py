#1-3
age = 20
height = 1.75
var = 2+1j
print("My age is", age, "years old and my height is ", height, "meters.")
print("The complex number is:", var)
print("The type of the complex number is:", type(var))

#4 calculate the area of a triangle
base = float(input("Enter base: "))
height = float(input("Enter height: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

#5 calculate the parameter of a triangle
side_a = float(input("Enter side a: "))
side_b = float(input("Enter side b: "))
side_c = float(input("Enter side c: "))
parameter = side_a + side_b + side_c
print("The parameter of the triangle is:", parameter)

#6 calculate the area and parameter of a rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
area = length * width
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

#7 calculate the area and circumference of a circle
radius = float(input("Enter radius: "))
area = 3.14 * (radius **2)
circumference = 3.14 * 2 * radius
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)

#8-9 calculate the slope of a line and euclidean distance between two points
x1 = float(input("Enter x1: "))
y1 = 2*x1 -2
x2 = float(input("Enter x2: "))
y2 = 2*x2 -2
slope1 = (y2-y1)/(x2-x1)
print("The slope of the line is:", slope1)
euclidean_distance = ((x2-x1)**2 + (y2-y1)**2)**0.5
print("The euclidean distance between the two points is:", euclidean_distance)

#10 compare the slopes of two lines
slope2 = 2
print("The slope of 8 and 9 is equal", slope2 == slope1)

#11 calculate the value of y for a given x in the equation y = x^2 + 6x + 9
x = float(input("Enter x: "))
y = x**2 + 6*x + 9
print("The value of y for the given x is:", y)

#12 find length of "python" and "dragon" and make a falsy comparison statement
word1 = "python"
word2 = "dragon"
print(len(word1) != len(word2))

#13 check if "on" is found in both "python" and "dragon"
print("on" in word1 and "on" in word2)

#14 check if "jargon" is found in the sentence
sentence = "I hope this course is not full of jargon."
print("jargon" in sentence)

#15 check if "on" is not found in both "python" and "dragon"
print(not("on" in word1 and "on" in word2))

#16 find the length of the string "python" and convert it to float and string
length = len(word1)
length = float(length)
length = str(length)
print("The length of 'python' is:", length)

#17 check if input number is even or not
number = input("Enter a number: ")
print("The number is even:", int(number) % 2 == 0)

#18 check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division = 7//3
int_value = int(2.7)
print("The floor division of 7 by 3 is equal to the int converted value of 2.7:", floor_division == int_value)

#19 check if type of '10' is equal to type of 10
print("The type of '10' is equal to the type of 10:", type('10') == type(10))

#20 check if int('9.8') is equal to 10
print("The int('9.8') is equal to 10:", int(float('9.8')) == 10)

#21 write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person.
hours = float(input("Enter hours: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print("Your weekly earning is:", pay)

#22 write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = int(input("Enter number of years you have lived: "))
seconds_per_year = 365 * 24 * 60 *60
seconds_lived = year * seconds_per_year
print("You have lived for ", seconds_lived, " seconds.")

#23 Write a Python script that displays the following table
print("1 1 1 1 1")
print("2 1 2 4 8")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")