import random

#useWabbajack = int(input("Use "))
#if useWabbajack == 1:

polymorph = ["Chicken", "Goat", "Swarm of Bees!", "Kobold", "Rabbit", "Owl", "Stein of Ale", "T-Rex"]
buffs = ["enlarge", "reduce", "haste", "freedom of movement", "invisibility"]
direction = ["in front of", "behind", "to the left of", "to the right of", "above"]
person = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"]
 
flipCoin = int(random.randint(0,1)) #for play set to 0,1
rollD100 = int(random.randint(0,99)) #for play set to 0,19
rollD20 = int(random.randint(19,19)) #for play set to 0,19
rollD10 = int(random.randint(1,10)) #for play set to 1,10
rollD8 = int(random.randint(1,8)) #for play set to 1,8
rollD5 = int(random.randint(1,5)) #for play set 1,5

rollPolymorph  = int(random.randint(0,len(polymorph)-1))
rollBuffs = int(random.randint(0,len(buffs)-1))
rollDirection = int(random.randint(0,len(direction)-1))
rollPerson = int(random.randint(0,len(person)-1))
rollDistanceNear = int(random.randint(1,5))

if rollD20 == 0:
    print("Fireball")
elif rollD20 == 1:
    print("Thunderbolt")
elif rollD20 == 2:
    print("Cone of Cold")
elif rollD20 == 3:
    flipCoin
    if flipCoin == 0:
        print("Heal self 10HP")
    else:
        print("Nearest enemy heals 10HP")
elif rollD20 == 4:
    rollD20
    print(str(int(rollD20+1))+str("gp falls from the sky"))
elif rollD20 == 5:
    rollD10
    if rollD10 == 1:
        print(str("You have been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute"))
    else:
        print(str("Nearest enemy has been turned into a ")+str(polymorph[rollPolymorph])+str(" for one minute"))
elif rollD20 == 6:
    flipCoin
    if flipCoin == 1:
        print("You are now invisible for one minute, or until you attack or until you take damage")
    else:
        print("Nearest enemy is now invisble for one minute, or until it attacks or takes damage")
elif rollD20 == 7:
    rollD10
    if rollD10 == 1:
        print("An enemy kobold appears")
    elif rollD10 == 2:
        print("A friendly kobold appears and aids you in combat for one day")
    else:
        print("A friendly kolbold appears and gives you 10 Silver and a pretty flower")
elif rollD20 == 8:
    print("All creatures, monsters, etc. Are knocked prone")
elif rollD20 == 9:
    print("Wabbajack Juice has been added to your inventory \nThe Effects of Wabbajack juice can only be revealed after consumption.")
#elif rollD20 = 10:
    #TBD
elif rollD20 == 11:
    rollD10
    if rollD10 == 1:
        print("You are frightened")
    else:
        print("Nearest enemy is now frightened of you")
elif rollD20 == 12:
    print("You take one level of exhaustion")
elif rollD20 == 13:
    rollBallbearings = int(random.randint(1,4))
    distanceBallbearings = int(random.randint(1,4))
    print(str(rollBallbearings)+str(" thousand ballbearings appear in ")+str(rollBallbearings)+str(" squares ")+str(distanceBallbearings)+str(" squares in front of you."))
elif rollD20 == 14:
    rollD5
    if rollD5 == 1:
        print("You have been sapped of 15hp and it has been given to the nearest enemy")
    else:
        print("You have absorbed 10hp from the nearest enemy")
#elif rollD20 = 15:
    #TBD
elif rollD20 == 16:
    rollBuffs
    rollD10
    print(str("You have been buffed with ")+str(buffs[rollBuffs]))
elif rollD20 == 17:
    rollD100
    if rollD100 == 99:
        print("Blazing wheels of cheese plummet to the ground at four different points you can see within one mile. Each creature in a 40-foot-radius sphere centered on each point you choose must make a Dexterity saving throw.\nThe sphere spreads around corners.\nA creature takes 20d6 fire damage and 20d6 bludgeoning damage on a failed save, or half as much damage on a successful one.\nA creature in the area of more than one fiery burst is affected only once.The spell damages objects in the area and ignites flammable objects that aren't being worn or carried.")
    else:
        print("Cheese rains down from on high pummeling your foes in a 10 foot area within 90 feet with 3d6 bludgeoning damage , or half as much upon a successful Dex save 18+")
elif rollD20 == 18:
    flipCoin
    rollD10
    if flipCoin == 0:
        print(str("You take ")+str(int(rollD10))+str(" damage"))
    else:
        print(str("The nearest enemy to you takes ")+str(int(rollD10))+str(" damage"))
elif rollD20 == 19:
    rollExplosionSize = int(random.randint(1,3))
    rollDistanceNear
    rollDirection
    rollPerson
    rollD10
    rollD20
    print(str("An explosion erupts ")+str(rollDistanceNear)+str(" squares ")+str(direction[rollDirection])+str(" ")+str(person[rollPerson])+str("\nAll creature, monsters, etc. within ")+str(rollExplosionSize)+str(" squares must beat a dexterity saving throw or take ")+str(rollD20)+str(" damage. Or half as much on successful save."))
