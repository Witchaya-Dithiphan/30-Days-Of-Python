# Create an empty dictionary called dog
dog = {}
# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = "Khaomao"
dog['color'] = ['White','Brown']
dog['breed'] = "Bangkaew"
dog['age'] = 7
print(dog)
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {'first_name':'Witchaya',
           'last_name':'Dithiphan',
           'gender':'male',
           'age':20,
           'marital':False,
           'status':'Alive',
           'skills':['C','Python','VHDL','C#','C++','Typescript','Javascript','CSS','React','SQL'],
           'country':'Thailand',
           'city':'Pattaya',
           'address':{'num':'115/1','moo':5,}}
print(student)
# Get the length of the student dictionary
print(len(student))
# Get the value of skills and check the data type, it should be a list
print(type(student['skills']))
# Modify the skills values by adding one or two skills
student['skills'].append('Github')
# Get the dictionary keys as a list
print(list(student.keys()))
# Get the dictionary values as a list
print(list(student.values()))
# Change the dictionary to a list of tuples using items() method
print(student.items())
# Delete one of the items in the dictionary
student.popitem()
print(student)
# Delete one of the dictionaries
del student['skills']
print(student)