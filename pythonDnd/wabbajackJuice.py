#D&D Wabbajack Juice by Diego Pisciotta, 2021

import random

potions = ["health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "potion of hill giant strength", "bone hurting juice"]
rollJuice = int(random.randint(0,len(potions)-1))

print(str(potions[rollJuice]))