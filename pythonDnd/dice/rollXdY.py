import random

def rollDice(diceToBeRolled, dX):
    rollDice = 0
    for x in range(diceToBeRolled):  
        diceValue = int(random.randint(1,dX))
        rollDice += diceValue
        x += 1
    # print (rollDice)
    return rollDice


print (rollDice(1,20))