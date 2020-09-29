partySize = int(input ("\nHow many players are in your party: "))

#These are the initial player inputs for the party loot to be divided and then optimised
partyPlatinum = int(input("\nPlatinum: "))
partyGold = int(input("Gold: "))
partySilver = int(input("Silver: "))
partyCopper = int(input("Copper: "))

platinum = partyPlatinum

# Gross gold
grossDividedGold = (partyGold + (platinum*10))
gold = grossDividedGold/partySize
goldRemaining = grossDividedGold-(partySize*gold)

# Gross Silver
grossDividedSilver = (partySilver + (goldRemaining*10))
silver = grossDividedSilver/partySize
silverRemaining = grossDividedSilver-(partySize*silver)

# Gross copper
grossDividedCopper = (partyCopper + (silverRemaining*10))
copper = grossDividedCopper/partySize
copperRemaining = grossDividedCopper-(partySize*copper)

print ("\nFor your convenience, platinum has been converted into gold.\n")
print(int(gold))
print(int(silver))
print(int(copper))
print(int(copperRemaining))