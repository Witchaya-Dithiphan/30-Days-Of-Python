# 1 Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
title = ['Thirty', 'Days', 'Of', 'Python']
print(' '.join(title))

# 2 Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
title = ['Coding', 'For' , 'All']
concat = ' '.join(title)
print(concat)
# 3 Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# 4 Print the variable company using print().
print(company)
# 5 Print the length of the company string using len() method and print().
print(len(company))
# 6 Change all the characters to uppercase letters using upper() method.
print(company.upper())
# 7 Change all the characters to lowercase letters using lower() method.
print(company.lower())
# 8 Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9 Cut(slice) out the first word of Coding For All string.
print(company[7:])
# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.index("Coding"))
# 11 Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding","Python"))
# 12 Change "Python for Everyone" to "Python for All" using the replace method or other methods.
print("Python for Everyone".replace("Everyone","All"))
# 13 Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))
# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
# 15 What is the character at index 0 in the string Coding For All.
print(company[0])
# 16 What is the last index of the string Coding For All.
print(len(company) - 1)
# 17 What character is at index 10 in "Coding For All" string.
print(company[10])
# 18 Create an acronym or an abbreviation for the name 'Python For Everyone'.
name = 'Python For Everyone'
words = name.split()
acronym = words[0][0]+words[1][0]+words[2][0]
print(acronym)
# 19 Create an acronym or an abbreviation for the name 'Coding For All'.
words = company.split()
acronym = words[0][0]+words[1][0]+words[2][0]
print(acronym)
# 20 Use index to determine the position of the first occurrence of C in Coding For All.
index = company.index('C')
print(index, company[index])
# 21 Use index to determine the position of the first occurrence of F in Coding For All.
index = company.index('F')
print(index, company[index])
# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
index = "Coding For All People".rfind('l')
print(index)
# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = "You cannot end a sentence with because because because is a conjunction"
index = sentence.find("because")
print(index)
# 24 Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
index = sentence.rfind("because")
print(index)
# 25 Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start = sentence.find('because')
end = sentence.rfind('because') + len('because')
print(sentence[start:end])  # ผลลัพธ์: 'because because because'
# 26 Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find("because"))
# 27 Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))
# 28 Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))
# 29 '   Coding For All      '  , remove the left and right trailing spaces in the given string.
sentence = '   Coding For All      '
print(sentence.strip())
# 30 Which one of the following variables return True when we use the method isidentifier():
#   30DaysOfPython
#   thirty_days_of_python
print("30DaysOfPython".isidentifier()) #False
print("thirty_days_of_python".isidentifier()) #True
# 31 The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("# ".join(lib))
# 32 Use the new line escape sequence to separate the following sentences.
#   I am enjoying this challenge.
#   I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")
# 33 Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
# 34 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print(f"radius = {radius}")
print(f"area = 3.14 * {radius} ** 2")
print(f"The area of a circle with radius {radius} is {int(area)} meters square.")
# 35 Make the following using string formatting methods:
a = 8
b = 6
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")
print(f"{a} % {b} = {a%b}")
print(f"{a} // {b} = {a//b}")
print(f"{a} ** {b} = {a**b}")