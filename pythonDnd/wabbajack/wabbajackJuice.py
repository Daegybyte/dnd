#D&D Wabbajack Juice by Diego Pisciotta, 2021
#Beta release
import random
import wabbajack as wj


potions = [
    "potion of greater healing.",
    "potion of hill giant strength. Your strength becomes 21 for one hour", 
    "potion of weakness. You lose 10 strength for one hour.",
    "bone hurting juice."
    ]

def drink_juice():
    rollJuice = int(random.randint(0,len(potions)-1))
    if rollJuice == 0:
        return(str("\nYou have consumed ")+str(potions[rollJuice]) + str("Regain ")+str(wj.rollDice(4,4)+4)+str(" health."))
    elif rollJuice == 3:
        return(str("\nYou have consumed ")+str(potions[rollJuice]) + str("Take ")+str(wj.rollDice(4,4)+4)+str(" damage."))
    else:
        return(str("\nYou have consumed ")+str(potions[rollJuice]))
