import random

potions = ["health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "health potion", "potion of hill giant strength", "bone hurting juice"]
rollJuice = int(random.randint(0,len(potions)-1))

#drinkWabbajackJuice = int(input("Drink Wabbajackjuice?: "))

#if drinkWabbajackJuice == 1:
print(str(potions[rollJuice]))