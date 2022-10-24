import sys
import re

name = input("Please enter your name: ")
age = input("Please enter your age: ")
fav_food = input("Please enter your favourite food: ")
fav_animal = input("Please enter your favourite animal: ")
result = 5/7

sys.stdout.write(name + "\n")
sys.stdout.write(age + "\n")
sys.stdout.write(fav_food + "\n")
sys.stdout.write(fav_animal)

sys.stdout.write(name + "\n" + age + "\n" + fav_food + "\n" + fav_animal + "\n")

sys.stdout.write(round(result, 1))
sys.stdout.write(round(result, 3))
sys.stdout.write(round(result, 5))
sys.stdout.write(round(result, 10))

