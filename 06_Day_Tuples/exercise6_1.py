# 1. Create an empty tuple
num = tuple()
# 2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sister = ('prae','prim')
brother = ('prompt',)
print(brother)
print(sister)
# 3. Join brothers and sisters tuples and assign it to siblings
siblings = sister + brother
print(siblings)
# 4. How many siblings do you have?
people = len(siblings)
print(people)
# 5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = list(siblings)
family_members.append('vichien')
family_members.append('weena')
family_members = tuple(family_members)
print(family_members)