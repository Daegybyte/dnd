import math
x = float(input("\nx to creature: "))
y = float(input("y to creature: "))
spellRange = float(input("spell/attack range: "))

def rangeFinder(xToTarg,yToTarg,rangeOfAttack):
    hyp = math.sqrt((x**2)+(y**2))
    if (spellRange>hyp):
        return "\ntarget in range"
    else:
        return "\ntarget out of range"

print (rangeFinder(x,y,spellRange))