#D&D Wabbajack by Diego Pisciotta, 2021
import random
import json

"""
* Once per short rest
* The wabbajack ignores all resistances, willingness requirements (polymorph),or saving throws unless otherwise specified.
This is because random nature of the Wabbajack essentially functions as the saving throw. The fact that it did not roll polymorph means you have in a sense beaten a DCnumberOfWabbajackEffects against it.
* Wabbajack Juice is a potion that magically appears in the player inventory. The effects are chosen after consumption and are most likely a health potion, but can be a potion of hill giant strength or a potion of poison
resleeved as Bone Hurting Juice. 
https://github.com/Daegybyte/dnd/blob/master/pythonDnd/wabbajack/wabbajackJuice.py
"""

# Lists to pull from
polymorph = ["chicken", "goat", "swarm of bees!", "kobold", "cat", "rabbit", "owl", "stein of ale","Bruce Willis", "dire wolf", "yeti", "raven", "polar bear", "T-Rex"]
buffs = ["enlarge", "reduce", "haste", "freedom of movement", "bardic inspiration"]
direction = ["in front of", "behind", "to the left of", "to the right of", "above"]
person = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"]
afraidOf = ["Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"] #copy of array person but the user/wabbajacker is removed to avoid making them fear themselves
party = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever"]
 
#Dice Rolls
wabbajackSelector = int(random.randint(0,18)) #for testing, set both numbers to the effect number you are testing. For play, set to '0,maxEffectNumber' ......More effects should be added
flipCoin = int(random.randint(0,1)) #for play set to 0,1
rollD100 = int(random.randint(1,100)) #for play set to 1,100
rollD20 = int(random.randint(1,20)) #for play set to 1,20
rollD10 = int(random.randint(1,10)) #for play set to 1,10
rollD8 = int(random.randint(1,8)) #for play set to 1,8
rollD6 = int(random.randint(1,6)) #for play set to 1,6
rollD5 = int(random.randint(1,5)) #for play set 1,5

# Do NOT touch
rollPolymorph  = int(random.randint(0,len(polymorph)-1))
rollBuffs = int(random.randint(0,len(buffs)-1))
rollDirection = int(random.randint(0,len(direction)-1))
rollPerson = int(random.randint(0,len(person)-1))
rollParty = int(random.randint(0,len(party)-1))
rollAfraidOf = int(random.randint(0,len(afraidOf)-1))
rollDistanceNear = int(random.randint(1,5))
rollDistanceMedium = int(random.randint(4,11))
rollDistanceFar = int(random.randint(9,18))

#function to output damage based on xDy format of rolling damage dice x,y
def rollDamage(diceToBeRolled, dX):
    rollDamage = 0
    for x in range(diceToBeRolled):  
        diceValue = int(random.randint(1,dX))
        rollDamage += diceValue
        x += 1
    return rollDamage

#fireball
if wabbajackSelector == 0: 
    flipCoin
    if flipCoin == 0:
        print(str("a fireball shoots towards ")+str(party[rollParty])+ str(" who takes ")+str(rollDamage(8,6))+str(" damage."))
    else:
        print(str("A fireball shoots towards the strongest enemy (determined by DM) who takes ")+str(rollDamage(8,6))+str(" damage"))
#lightning bolt
elif wabbajackSelector == 1:
    print(str("A lightning bolt shoots towards the nearest enemy who takes ")+str(rollDamage(3,6))+str(" damage"))
#Ice storm
elif wabbajackSelector == 2:
    flipCoin
    rollD10
    if flipCoin == 1:
        print(str("A ")+str(rollD10)+str(" square diameter ice storm centred on the nearest enemy. All creatures in area take 4d6 damage."))
    else:
        print(str("A ")+str(rollD10)+str(" square diameter ice storm centred on the farthest enemy. All creatures in area take 4d6 damage."))
#Heal
elif wabbajackSelector == 3:
    flipCoin
    if flipCoin == 0:
        print("Heal self 10HP")
    # maybe add a 1/100 chance to full heal party
    else:
        print("Nearest enemy heals 10HP")
#Make it rain
elif wabbajackSelector == 4:
    rollD20
    print(str(int(rollD20))+str("gp falls from the sky"))
#Polymorph
elif wabbajackSelector == 5:
    rollD10
    if rollD10 <= 4:
        print(str(party[rollParty])+str(" has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute"))
    else:
        print(str("Nearest enemy has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute"))
#Invisibility
elif wabbajackSelector == 6:
    flipCoin
    if flipCoin == 1:
        print("You are now invisible for one minute, or until you attack or until you take damage")
    else:
        print("Nearest enemy is now invisble for one minute, or until it attacks or takes damage")
#Summon Kobold
elif wabbajackSelector == 7:
    rollD10
    if rollD10 == 1:
        print("An enemy kobold appears")
    elif rollD10 == 2:
        print("A friendly kobold appears and aids you in combat for one day")
    else:
        print("A friendly kolbold appears and gives you 10 Silver and a pretty flower")
#Prone
elif wabbajackSelector == 8:
    print("All creatures, monsters, etc. Are knocked prone")
#Wabbajack Juice 
elif wabbajackSelector == 9:
    rollParty
    rollD5
    if rollD5 <= 3:
        print(str("Wabbajack juice has been added to ")+str(party[rollParty])+str("'s inventory.\nThe effects of Wabbajack juice can only be revealed after consumption.\nPrevious wabbajack juice disappears from inventory if it has not been consumed by the time the wabbajack is used again."))
    else:
        print("Wabbajack Juice has been added to your inventory \nThe effects of Wabbajack juice can only be revealed after consumption.\nPrevious wabbajack juice disappears from inventory if it has not been consumed by the time the wabbajack is used again.")
#Fear
elif wabbajackSelector == 10:
    rollD10
    if rollD10  <= 3:
        print(str("You are frightened of ")+str(afraidOf[rollAfraidOf])+str(" for one minute"))
    else:
        print("Nearest enemy is now frightened of you for one minute")
#Exhaustion
elif wabbajackSelector == 11:
    print("You take one level of exhaustion")
#Ballbearings
elif wabbajackSelector == 12:
    rollBallbearings = int(random.randint(1,4))
    distanceBallbearings = int(random.randint(1,4))
    print(str(rollBallbearings)+str(" thousand ballbearings appear in ")+str(rollBallbearings)+str(" squares ")+str(distanceBallbearings)+str(" ")+str(direction[rollDirection])+str(" ")+str(person[rollPerson]))
#Absorb HP
elif wabbajackSelector == 13:
    rollD5
    if rollD5 == 1:
        print("You have been sapped of 15hp and it has been given to the nearest enemy")
    else:
        print("You have absorbed 10hp from the nearest enemy")
#Buffs
elif wabbajackSelector == 14:
    rollBuffs
    rollD10
    if rollD10 <= 2:
        print(str(person[rollPerson])+str(" has been buffed with ")+str(buffs[rollBuffs]))
    else:
        print(str("You have been buffed with with ")+str(buffs[rollBuffs]))
#Cheese storm
elif wabbajackSelector == 15:
    rollD100
    if rollD100 == 100:
        print("Blazing wheels of cheese plummet to the ground at four different points you can see within one mile. Each creature in a 40-foot-radius sphere centered on each point you choose must make a Dexterity saving throw.\nThe sphere spreads around corners.\nA creature takes 40d6 damage on a failed save, or half as much damage on a successful one.\nA creature in the area of more than one fiery burst is affected only once.The spell damages objects in the area and ignites flammable objects that aren't being worn or carried.")
    else:
        print("Cheese rains down from on high pummeling your foes in a 10 foot area within 90 feet with 3d6 damage , or half as much upon a successful save Dex 18")
#Random Damage
elif wabbajackSelector == 16:
    flipCoin
    rollD10
    if flipCoin == 0:
        print(str("You take ")+str(int(rollD10))+str(" damage"))
    else:
        print(str("The nearest enemy to you takes ")+str(int(rollD10))+str(" damage"))
#Explosion
elif wabbajackSelector == 17:
    rollExplosionSize = int(random.randint(1,3))
    rollDistanceNear
    rollDirection
    rollPerson
    rollD10
    rollD20
    print(str("An explosion erupts ")+str(rollDistanceNear)+str(" squares ")+str(direction[rollDirection])+str(" ")+str(person[rollPerson])+str("\nAll creature, monsters, etc. within ")+str(rollExplosionSize)+str(" squares must beat a dexterity saving throw or take ")+str(rollD20)+str(" damage. Or half as much on successful save."))

#Lucky

elif wabbajackSelector == 18:
    print(str(party[rollParty])+str(" has become luckyfor one day!\nYou have 3 luck points. Whenever you make an attack roll, ability check, or saving throw, you may spend 1 luck point to roll an additional d20. You can use this ability after the original roll, but before the outcome is revealed. You choose which of the d20s is used for the attack roll, ability check, or saving throw.\nYou can also spend one luck point when an attack roll is made against you. Roll a d20, and choose whether the attacker's roll uses their d20 roll or yours.\nIf multiple creatures use a luck point on the same roll, they cancel out, resulting in no additional dice.\n"))

#spectral shield
elif wabbajackSelector == 19:
     print(str("A spectral shield appears near ")+str(party[rollParty])+str(". Their AC is increased by +2\nand they are immune to magic missile for one minute."))