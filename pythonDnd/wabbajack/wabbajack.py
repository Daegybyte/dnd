#D&D Wabbajack by Diego Pisciotta, 2021
#Beta release
import random
import json


#How to use:
"""
* Once per short rest

* The wabbajack ignores all resistances, willingness requirements (polymorph),or saving throws unless otherwise specified.
This is because random nature of the Wabbajack essentially functions as the saving throw.
The fact that it did not roll polymorph means you have in a sense beaten a DCnumberOfWabbajackEffects.

* Wabbajack Juice is a potion that magically appears in the player inventory.
The effects are chosen after consumption. But can be a greater restoration potion, but can be of hill giant strength,
weakness, or of poison resleeved as Bone Hurting Juice. 
The script for  Wabbajack Juice can be found at: https://github.com/Daegybyte/dnd/blob/master/pythonDnd/wabbajack/wabbajackJuice.py
"""

#About the Wabbajack:
"""
The Wabbajack was forged sometime in the age of demons. However origins of it and its creator have become lost in the mist of time.
There are mentions here and there of it in obscure books, scrolls, and old stories told in remote corners of the world.
For the few who have heard of it, most believe it to be a myth.

The Wabbajackl has been lost and found countless times through the millenia. Though most who came across it did not know it.
The only constant is that sooner or later, like the one ring, it betrayed the one who wields it as it waits for its master to return.
"""

#Lists to pull from
party = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever"]
person = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"]
afraidOf = ["Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"] #copy of array person but the user/wabbajacker is removed to avoid making them fear themselves
polymorph = ["chicken", "goat", "swarm of bees!", "a friendly dog", "cat","death dog", "cockatrice","gelatinous cube",
"rabbit","shadow", "owl", "zombie", "stein of ale","Bruce Willis", "beholder",
"dire wolf", "yeti", "raven", "bowl of petunias", "polar bear", "big ol' nasty lizard boi"]
buffs = ["enlarge", "reduce", "haste", "freedom of movement", "bardic inspiration"]
direction = ["squares north", "squares south", "squares east", "squares west"]
squares = ["one", "two", "three", "four", "five"]

 
#Dice Rolls

# For play, set to (1,20)
#for testing, set both numbers to the effect number you are testing.
wabbajackSelector = int(random.randint(1,20)) 
flipCoin = int(random.randint(0,1))

#function to output dice rolls based on xDy format of rolling damage dice x,y
def rollDice(diceToBeRolled, dX):
    sumDice = 0
    for x in range(diceToBeRolled):  
        diceValue = int(random.randint(1,dX))
        sumDice += diceValue
        x += 1
    return sumDice

rollBallbearings = int(random.randint(1,4)) #spawns 1,2,3,4 thousand ballbearings
rollDistanceNear = int(random.randint(1,5))
#rollDistanceMedium = int(random.randint(4,11))
#rollDistanceFar = int(random.randint(9,18))

# Do NOT touch
rollPolymorph  = int(random.randint(0,len(polymorph)-1))
rollBuffs = int(random.randint(0,len(buffs)-1))
rollDirection = int(random.randint(0,len(direction)-1))
rollSquares = int(random.randint(0,len(squares)-1))
rollPerson = int(random.randint(0,len(person)-1))
rollParty = int(random.randint(0,len(party)-1))
rollAfraidOf = int(random.randint(0,len(afraidOf)-1))



#Wabbajack effects:

#lightning bolt
if wabbajackSelector == 1:
    print(str("\nA lightning bolt shoots towards the nearest enemy who takes ")+str(rollDice(3,6))+str(" damage.\nFlammable objects within 5 feet not being worn or carried burst into flame"))

#Ice storm
elif wabbajackSelector == 2:
    flipCoin
    if flipCoin == 1:
        print(str("\n")+str("A ")+str(rollDice(1,5))+str(" square radius ice storm centred on the nearest enemy. All creatures in area take ")+str(rollDice(4,6))+str(" damage.\nThe ground is now difficult icy terrain.\n"))
    else:
        print(str("\n")+str("A ")+str(rollDice(1,5))+str(" square radius ice storm centred on the farthest enemy. All creatures in area take ")+str(rollDice(4,6))+str(" damage.\nThe ground is now difficult icy terrain.\n"))

#Heal
elif wabbajackSelector == 3:
    if rollDice(1,100) == 100:
        print(str("\nParty regains full health, plus ")+str(int(rollDice(1,8)))+str(" temporary hit points.\n"))
    elif rollDice(1,100) <= 50:
        print("\nNearest enemy heals 15HP.\n")
    else:
        print(str("\n")+str(str(party[rollParty]))+str(" heals 10HP.\n"))   

#Make it rain
elif wabbajackSelector == 4:
    print(str("\n")+str(int(rollDice(1,20)))+str("gp fall from the sky.\n"))

#Polymorph
elif wabbajackSelector == 5:
    if rollDice(1,10) <= 4:
        print(str("\n")+str(party[rollParty])+str(" has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute.\n"))
    elif rollDice(1,10) == 5:
        print(str("\n")+str("Strongest enemy (determined by DM) has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute.\n"))
    else:
        print(str("\n")+str("Nearest enemy has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute.\n"))

#Invisibility
elif wabbajackSelector == 6:
    flipCoin
    if flipCoin == 1:
        print(str("\n")+str(party[rollParty])+str(" is now invisible for one minute, or until they attack or until they take damage.\n"))
    else:
        print(str("\n")+str("The nearest enemy to ")+str(party[rollParty])+str(" is now invisible for one minute, or until it attacks or takes damage.\n"))

#Summon Kobold
elif wabbajackSelector == 7:
    if rollDice(1,10) == 1:
        print(str("\n")+str("An enemy kobold appears!\n"))
    elif rollDice(1,10) == 2:
        print(str("\n")+str("A friendly kobold appears and aids you in combat for one day.\n"))
    else:
        print(str("\n")+str("A friendly kolbold appears and gives ")+str(party[rollParty])+str(" ")+str(rollDice(3,6))+str(" silver and a pretty flower.\n"))

#Prone
elif wabbajackSelector == 8:
    print(str("\n")+str("All standing creatures, monsters, etc. are knocked prone. All flying creatures are forced to land.\n"))

#Wabbajack Juice 
elif wabbajackSelector == 9:
    print(str("\nWabbajack juice appears in ")+str(party[rollParty])+str("'s hand.\nThey can either take one action to put it away\nor consume without using an action.\n\nThe effects of Wabbajack juice can only be revealed after consumption.\nPrevious wabbajack juice disappear from existence if it has not been consumed\nby the time the wabbajack is used again.\n"))

#Fear
elif wabbajackSelector == 10:
    if rollDice(1,10)  <= 3:
        print(str("\n")+str("You are frightened of ")+str(afraidOf[rollAfraidOf])+str(" for one minute.\n"))
    else:
        print(str("\n")+str("The nearest enemy to ")+str(party[rollParty])+str(" is now frightened of them for one minute.\n"))

#Exhaustion
elif wabbajackSelector == 11:
    print(str("\n")+str(party[rollParty])+str(" takes one level of exhaustion.\n"))

#Ballbearings
elif wabbajackSelector == 12:
    rollBallbearings
    rollSquares
    print(str("\n")+str(rollBallbearings)+str(" thousand ballbearings appear in ")+str(rollBallbearings)+str(" squares,\n")+str(squares[rollSquares])+str(" ")+str(direction[rollDirection])+str(" of ")+str(person[rollPerson])+str(".\n"))

#Absorb HP
elif wabbajackSelector == 13:
    if rollDice(1,5) == 1:
        print(str("\n")+str("You have been sapped of 15hp and it has been given to the nearest enemy.\n"))
    else:
        print(str("\n")+str("You have absorbed 10hp from the nearest enemy.\n"))

#Buffs
elif wabbajackSelector == 14:
    rollBuffs
    if rollDice(1,10) <= 3:
        print(str("\n")+str(person[rollPerson])+str(" has been buffed with ")+str(buffs[rollBuffs])+str(" for one minute.\n"))
    else:
        print(str("\n")+str("Selsys been buffed with with ")+str(buffs[rollBuffs])+str(" for one minute.\n"))

#Cheese storm
elif wabbajackSelector == 15:
    if rollDice(1,100) == 1:
        print(str("\nBlazing wheels of cheese plummet to the ground at four different points you can see within one mile.\n\nEach creature in a 40-foot-radius sphere centered on each point you choose must make a Dexterity saving throw.\nThe sphere spreads around corners.\nA creature takes ")+str(int(rollDice(40,6)))+str(" damage. on a failed save, or half as much damage on a successful one.\nA creature in the area of more than one fiery burst is affected only once.\nThe spell damages objects in the area and ignites flammable objects that aren't being worn or carried.\n"))
    else:
        print(str("\nCheese rains down from on high pummeling your foes in a ")+str(int(rollDice(2,5)))+str(" square area within 90 feet with ")+str(int(rollDice(3,6)))+str(" damage.\n"))

#Random Damage
elif wabbajackSelector == 16:
    flipCoin
    if flipCoin == 0:
        print(str("\n")+str(party[rollParty])+str(" takes ")+str(int(rollDice(2,6)))+str(" damage.\n"))
    else:
        print(str("\nThe nearest enemy to ")+str(party[rollParty])+str(" you takes ")+str(int(rollDice(3,6)))+str(" damage.\n"))

#Explosion
elif wabbajackSelector == 17:
    rollExplosionSize = int(random.randint(1,3))
    rollDistanceNear
    rollDirection
    rollPerson
    print(str("\nAn explosion erupts ")+str(rollDistanceNear)+str(" ")+str(direction[rollDirection])+str(" ")+str(person[rollPerson])+str("\nAll creature, monsters, etc. within ")+str(rollExplosionSize)+str(" squares radius must beat a dexterity saving throw 18 or take ")+str(rollDice(3,8))+str(" damage. Or half as much on successful save.\n"))

#Lucky
elif wabbajackSelector == 18:
    print(str("\n")+str(party[rollParty])+str(" has become lucky for one day!\n\nThey have 3 luck points. Whenever they make an attack roll, ability check, or saving throw, they may spend 1 luck point to roll an additional d20.\nThey can use this ability after the original roll,\nbut before the outcome is revealed. They choose which of the d20s is used for the attack roll, ability check, or saving throw.\nThey can also spend one luck point when an attack roll is made against them. Roll a d20, and choose whether the attacker's roll uses their d20 roll or the players.\nIf multiple creatures use a luck point on the same roll, they cancel out, resulting in no additional dice.\n"))

#Spectral Shield
elif wabbajackSelector == 19:
     print(str("\n")+str("A spectral shield appears near ")+str(party[rollParty])+str(". Their AC is increased by +2\nand they are immune to magic missile for one minute.\n"))

#Fireball
elif wabbajackSelector == 20: 
    flipCoin
    if flipCoin == 0:
        print(str("\nA fireball shoots towards ")+str(party[rollParty])+ str(" who takes ")+str(rollDice(8,6))+str(" damage.\n"))
    else:
        print(str("\nA fireball shoots towards the strongest enemy (determined by DM) who takes ")+str(rollDice(8,6))+str(" damage.\n"))