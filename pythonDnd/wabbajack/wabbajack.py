#D&D Wabbajack by Diego Pisciotta, 2021
#Beta release
import random
import json

"""
How to use:
* Once per short rest

* The wabbajack ignores all resistances, willingness requirements (polymorph),or saving throws unless otherwise specified.
This is because random nature of the Wabbajack essentially functions as the saving throw.
The fact that it did not roll polymorph means you have in a sense beaten a DCnumberOfWabbajackEffects.

* Wabbajack Juice is a potion that magically appears in the player inventory.
The effects are chosen after consumption. But can be a greater restoration potion, but can be aof hill giant strength,
weakness, or of poison resleeved as Bone Hurting Juice. 
The script for  Wabbajack Juice can be found at: https://github.com/Daegybyte/dnd/blob/master/pythonDnd/wabbajack/wabbajackJuice.py
"""

#Lists to pull from
party = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever"]
person = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"]
afraidOf = ["Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"] #copy of array person but the user/wabbajacker is removed to avoid making them fear themselves
polymorph = ["chicken", "goat", "swarm of bees!", "kobold", "cat", "rabbit", "owl", "stein of ale","Bruce Willis", "dire wolf", "yeti", "raven", "polar bear", "T-Rex"]
buffs = ["enlarge", "reduce", "haste", "freedom of movement", "bardic inspiration"]
direction = ["squares north", " squares south", "squares east", "squares west"]
squares = ["one", "two", "three", "four", "five"]

 
#Dice Rolls

#for testing, set both numbers to the effect number you are testing.
# For play, set to '1,maxEffectNumber' ......More effects should be added
wabbajackSelector = int(random.randint(18,18)) 
flipCoin = int(random.randint(0,1)) #for play set to 0,1

#function to output dice rolls based on xDy format of rolling damage dice x,y
def rollDice(diceToBeRolled, dX):
    rollDice = 0
    for x in range(diceToBeRolled):  
        diceValue = int(random.randint(1,dX))
        rollDice += diceValue
        x += 1
    return rollDice

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
    print(str("\nA lightning bolt shoots towards the nearest enemy who takes ")+str(rollDice(3,6))+str(" damage"))

#Ice storm
elif wabbajackSelector == 2:
    flipCoin
    if flipCoin == 1:
        print(str("\n")+str("A ")+str(rollDice(1,5))+str(" square radius ice storm centred on the nearest enemy. All creatures in area take ")+str(rollDice(4,6))+str(" damage.\nThe ground is now difficult terrain."))
    else:
        print(str("\n")+str("A ")+str(rollDice(1,5))+str(" square radius ice storm centred on the farthest enemy. All creatures in area take ")+str(rollDice(4,6))+str(" damage.\nThe ground is now difficult terrain"))

#Heal
elif wabbajackSelector == 3:
    if rollDice(1,100) == 100:
        print(str("\nParty regains full health, plus ")+str(int(rollDice(1,8)))+str(" temporary hit points"))
    elif rollDice(1,100) <= 50:
        print("\nNearest enemy heals 15HP")
    else:
        print(str("\n")+str(str(party[rollParty]))+str(" heals 10HP"))   

#Make it rain
elif wabbajackSelector == 4:
    print(str("\n")+str(int(rollDice(1,20)))+str("gp falls from the sky"))

#Polymorph
elif wabbajackSelector == 5:
    if rollDice(1,10) <= 4:
        print(str("\n")+str(party[rollParty])+str(" has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute"))
    elif rollDice(1,10) == 5:
        print(str("\n")+str("Strongest enemy (determined by DM) has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute"))
    else:
        print(str("\n")+str("Nearest enemy has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute"))

#Invisibility
elif wabbajackSelector == 6:
    flipCoin
    if flipCoin == 1:
        print(str("\n")+str(party[rollParty])+str(" is now invisible for one minute, or until they attack or until they take damage"))
    else:
        print(str("\n")+str("Nearest enemy is now invisble for one minute, or until it attacks or takes damage"))

#Summon Kobold
elif wabbajackSelector == 7:
    if rollDice(1,10) == 1:
        print(str("\n")+str("An enemy kobold appears"))
    elif rollDice(1,10) == 2:
        print(str("\n")+str("A friendly kobold appears and aids you in combat for one day"))
    else:
        print(str("\n")+str("A friendly kolbold appears and gives you 10 Silver and a pretty flower"))

#Prone
elif wabbajackSelector == 8:
    print(str("\n")+str("All creatures, monsters, etc. are knocked prone"))

#Wabbajack Juice 
elif wabbajackSelector == 9:
    flipCoin
    if flipCoin == 0:
        print(str("\nWabbajack juice has been added to ")+str(party[rollParty])+str("'s inventory.\nThe effects of Wabbajack juice can only be revealed after consumption.\nPrevious wabbajack juice disappears from inventory if it has not been consumed by the time the wabbajack is used again."))
    else:
        print("\nWabbajack Juice has been added to your inventory \nThe effects of Wabbajack juice can only be revealed after consumption.\nPrevious wabbajack juice disappears from inventory if it has not been consumed by the time the wabbajack is used again.")

#Fear
elif wabbajackSelector == 10:
    if rollDice(1,10)  <= 3:
        print(str("\n")+str("You are frightened of ")+str(afraidOf[rollAfraidOf])+str(" for one minute"))
    else:
        print(str("\n")+str("Nearest enemy is now frightened of you for one minute"))

#Exhaustion
elif wabbajackSelector == 11:
    print(str("\n")+str(party[rollParty])+str(" takes one level of exhaustion"))

#Ballbearings
elif wabbajackSelector == 12:
    rollBallbearings
    rollSquares
    print(str("\n")+str(rollBallbearings)+str(" thousand ballbearings appear in ")+str(rollBallbearings)+str(" squares, ")+str(squares[rollSquares])+str(" ")+str(direction[rollDirection])+str(" of ")+str(person[rollPerson]))

#Absorb HP
elif wabbajackSelector == 13:
    if rollDice(1,5) == 1:
        print(str("\n")+str("You have been sapped of 15hp and it has been given to the nearest enemy"))
    else:
        print(str("\n")+str("You have absorbed 10hp from the nearest enemy"))

#Buffs
elif wabbajackSelector == 14:
    rollBuffs
    if rollDice(1,10) <= 3:
        print(str("\n")+str(person[rollPerson])+str(" has been buffed with ")+str(buffs[rollBuffs]))
    else:
        print(str("\n")+str("You have been buffed with with ")+str(buffs[rollBuffs]))

#Cheese storm
elif wabbajackSelector == 15:
    if rollDice(1,100) == 1:
        print(str("\nBlazing wheels of cheese plummet to the ground at four different points you can see within one mile.\n\nEach creature in a 40-foot-radius sphere centered on each point you choose must make a Dexterity saving throw.\nThe sphere spreads around corners.\nA creature takes ")+str(int(rollDice(40,6)))+str(" damage on a failed save, or half as much damage on a successful one.\nA creature in the area of more than one fiery burst is affected only once.\nThe spell damages objects in the area and ignites flammable objects that aren't being worn or carried."))
    else:
        print(str("\nCheese rains down from on high pummeling your foes in a ")+str(int(rollDice(2,5)))+str(" square area within 90 feet with ")+str(int(rollDice(3,6)))+str(" damage , or half as much upon a successful save Dex 18"))

#Random Damage
elif wabbajackSelector == 16:
    flipCoin
    if flipCoin == 0:
        print(str("\nYou take ")+str(int(rollDice(2,6)))+str(" damage"))
    else:
        print(str("\nThe nearest enemy to you takes ")+str(int(rollDice(3,6)))+str(" damage"))

#Explosion
elif wabbajackSelector == 17:
    rollExplosionSize = int(random.randint(1,3))
    rollDistanceNear
    rollDirection
    rollPerson
    print(str("\nAn explosion erupts ")+str(rollDistanceNear)+str(" ")+str(direction[rollDirection])+str(" ")+str(person[rollPerson])+str("\nAll creature, monsters, etc. within ")+str(rollExplosionSize)+str(" squares must beat a dexterity saving throw 18 or take ")+str(rollDice(3,8))+str(" damage. Or half as much on successful save."))

#Lucky
elif wabbajackSelector == 18:
    print(str("\n")+str(party[rollParty])+str(" has become lucky for one day!\nThey have 3 luck points. Whenever they make an attack roll, ability check, or saving throw, they may spend 1 luck point to roll an additional d20.\nThey can use this ability after the original roll,\nbut before the outcome is revealed. They choose which of the d20s is used for the attack roll, ability check, or saving throw.\nThey can also spend one luck point when an attack roll is made against them. Roll a d20, and choose whether the attacker's roll uses their d20 roll or the players.\nIf multiple creatures use a luck point on the same roll, they cancel out, resulting in no additional dice.\n"))

#spectral shield
elif wabbajackSelector == 19:
     print(str("\n")+str("A spectral shield appears near ")+str(party[rollParty])+str(". Their AC is increased by +2\nand they are immune to magic missile for one minute."))

#fireball
elif wabbajackSelector == 20: 
    flipCoin
    if flipCoin == 0:
        print(str("\na fireball shoots towards ")+str(party[rollParty])+ str(" who takes ")+str(rollDice(8,6))+str(" damage."))
    else:
        print(str("\nA fireball shoots towards the strongest enemy (determined by DM) who takes ")+str(rollDice(8,6))+str(" damage"))