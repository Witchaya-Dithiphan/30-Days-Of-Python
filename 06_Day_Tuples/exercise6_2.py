# Exercises: Level 2
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
family_members = ('prae', 'prim', 'prompt', 'vichien', 'weena')
# 1. Unpack siblings and parents from family_members
*siblings, father, mother = family_members
print(siblings)
print(father)
print(mother)
# 2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('egg','milk','yogurt','cheese','meat','pork')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
# 3. Change the about food_stuff_tp  tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
# 4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
mid = len(food_stuff_tp)//2
print(food_stuff_tp[mid])
# 5. Slice out the first three items and the last three items from food_stuff_lt list
print(food_stuff_lt[:3])
print(food_stuff_lt[len(food_stuff_lt)-3:])
# 6. Delete the food_stuff_tp tuple completely
del food_stuff_tp
# 7. Check if an item exists in  tuple:
# - Check if 'Estonia' is a nordic country
# - Check if 'Iceland' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)