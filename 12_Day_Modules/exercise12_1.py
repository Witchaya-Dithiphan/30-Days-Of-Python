# Write a function which generates a six digit/character random_user_id.
#   print(random_user_id()) 
#   '1ee33d'
from random import choice , randint
import string
def random_user_id(length = 6):
    characters = [i for i in string.ascii_lowercase]
    digits = [i for i in string.digits]
    user_id = ""
    for i in range(length):
        ran_index = randint(0,1)
        if ran_index == 0:
            ran_char = randint(0,25)
            user_id += characters[ran_char]
        elif ran_index == 1:
            ran_digit = randint(0,9)
            user_id += digits[ran_digit]
    return user_id

def random_user_id2(length = 5):
    char_pool = string.ascii_lowercase + string.digits
    user_id = ""

    for _ in range(length):
        user_id += choice(char_pool)
    return user_id
print(random_user_id(8))
print(random_user_id2(100))

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
# print(user_id_gen_by_user()) # user input: 5 5
# #output:
# #kcsy2
# #SMFYb
# #bWmeq
# #ZXOYh
# #2Rgxf

# print(user_id_gen_by_user()) # 16 5
# #1GCSgPLMaBAVQZ26
# #YD7eFwNQKNs7qXaT
# #ycArC5yrRupyG00S
# #UbGxOFI7UXSWAyKN
# #dIV0SSUTgAdKwStr

def user_id_gen_by_user():
    char_len = int(input("Enter number of characters: "))
    num_ids = int(input("Enter number of IDs: "))
    for _ in range(num_ids):
        print(random_user_id(char_len))
user_id_gen_by_user()  

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
# print(rgb_color_gen())
# # rgb(125,244,255) - the output should be in this form

def rgb_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return f"rgb({r},{g},{b})"
print(rgb_color_gen())