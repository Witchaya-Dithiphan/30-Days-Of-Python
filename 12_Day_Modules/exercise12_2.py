# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
import string
from random import choice , randint

def list_of_hexa_colors(n):
    hexa = string.digits + "ABCDEF"
    colors = []
    for _ in range(n):
        color = "#"
        for i in range(6):
            color+=choice(hexa)
        colors.append(color)
    return colors
print(list_of_hexa_colors(3))

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def rgb_color_gen():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return f"rgb({r},{g},{b})"

def list_of_rgb_colors(n):
    rgb_colors = []
    for _ in range(n):
        rgb_colors.append(rgb_color_gen())
    return rgb_colors
print(list_of_rgb_colors(3))
# Write a function generate_colors which can generate any number of hexa or rgb colors.
#    generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
#    generate_colors('hexa', 1) # ['#b334ef']
#    generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
#    generate_colors('rgb', 1)  # ['rgb(33,79, 176)']

def generate_colors(types,n):
    if types == "hexa":
        print(list_of_hexa_colors(n))
    elif types == "rgb":
        print(list_of_rgb_colors(n))

generate_colors('hexa', 3)
generate_colors('hexa', 1)
generate_colors('rgb', 3)
generate_colors('rgb', 1)