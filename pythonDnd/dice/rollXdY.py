import random

def rollDamage(diceToBeRolled, dX):
    rollDamage = 0
    for x in range(diceToBeRolled):  
        diceValue = int(random.randint(1,dX))
        rollDamage += diceValue
        x += 1
    print(rollDamage)
    return rollDamage


print(rollDamage(1,6))