import math
x = float(input("\nx to creature: "))
y = float(input("y to creature: "))
spellRange = int(input("spell range: "))

def rangeFinder(x,y,spellRange):
    hyp = math.sqrt((x**2)+(y**2))
    if (spellRange>hyp):
        return "\ntarget in range"
    else:
        return "\ntarget out of range"

print (rangeFinder(x,y,spellRange))