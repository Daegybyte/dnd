#D&D Wabbajack Juice by Diego Pisciotta, 2021
#Beta release
import random


#function to output dice rolls based on xDy format of rolling damage dice x,y
def rollDice(diceToBeRolled, dX):
    rollDice = 0
    for x in range(diceToBeRolled):  
        diceValue = int(random.randint(1,dX))
        rollDice += diceValue
        x += 1
    return rollDice
potions = [
    "potion of greater healing.",
    "potion of hill giant strength.\nYour strength becomes 21 for one hour", 
    "potion of weakness.\nYou lose 10 strength for one hour.",
    "bone hurting juice."
    ]
rollJuice = int(random.randint(0,len(potions)-1))

print(str("\nYou have consumed ")+str(potions[rollJuice]))
if rollJuice == 0:
    print(str("Regain ")+str(rollDice(4,4)+4)+str(" health."))
if rollJuice == 3:
    print(str("Take ")+str(rollDice(4,4)+4)+str(" damage."))