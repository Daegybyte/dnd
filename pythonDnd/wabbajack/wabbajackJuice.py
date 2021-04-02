#D&D Wabbajack Juice by Diego Pisciotta, 2021
import random

potions = ["potion of greater healing regain 4d4+4 health", "potion of hill giant strength. Your strength becomes 21 for one hour", "bone hurting juice. Take 4d4 damage", "weakness????"]
rollJuice = int(random.randint(0,len(potions)-1))

print(str("You have consumed ")+str(potions[rollJuice]))