# Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
if 'skills' in person:
    mid = len(person['skills'])//2
    skills = person['skills'][mid]
    print(skills)
#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if 'skills' in person:
    if 'Python' in person['skills']:
        print("This person have Python skill")
    else:
        print("This person does not have Python skill")
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
skills = set(person['skills'])
if set(['React', 'Node', 'MongoDB']).issubset(skills):
    print('He is a fullstack developer')
elif set(['Node','Python','MongoDB']).issubset(skills):
    print('He is a backend developer')
elif set(['JavaScript','React']).issubset(skills):  
    print('He is a frontend developer')
else:
    print('unknown title')
#  * If the person is married and if he lives in Finland, print the information in the following format:
    # Asabeneh Yetayeh lives in Finland. He is married.
if person['is_married'] == True and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")