import random

def rollDamage(diceToBeRolled, dX):
    rollDamage = 0
    for x in range(diceToBeRolled):  
        rollD6 = int(random.randint(1,dX))
        rollDamage += rollD6
        x += 1
    print(rollDamage)
    return rollDamage


print(rollDamage(3,3))