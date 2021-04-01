import random

potions = ["health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "potion of hill giant strength", "bone hurting juice"]
rollJuice = int(random.randint(0,len(potions)-1))

print(str(potions[rollJuice]))