import random

buffs = ["enlarge","reduce","haste","freedom of movement","invisibility"]

rollBuffs = int(random.randint(0,len(buffs)-1))
rollD10 = int(random.randint(1,10))

print(rollBuffs)

print(str("You have been buffed with ")+str(buffs[rollBuffs]))