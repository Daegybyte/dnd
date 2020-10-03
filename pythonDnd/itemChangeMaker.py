#!/usr/bin/env python
import py_compile

y = True
while (y):

    print("\nHow much is the item?\n")

    goldPrice = int(input("Gold: "))
    silverPrice = int(input("Silver: "))
    copperPrice = int(input("Copper "))

    goldPrice = goldPrice*100 #Convert gold to copper
    silverPrice = silverPrice*10 #Convert silver to copper

    print("\nHow much did you pay?\n")
    goldPaid = int(input("Gold: "))
    silverPaid = int(input("Silver: "))
    copperPaid = int(input("Copper "))

    goldPaid = goldPaid*100
    silverPaid = silverPaid*10

    combinedPriceInCopper = goldPrice + silverPrice + copperPrice
    combinedPaidInCopper = goldPaid + silverPaid + copperPaid


    if combinedPaidInCopper >= combinedPriceInCopper:
    
        changeDue = combinedPaidInCopper - combinedPriceInCopper

        goldToPlayer = changeDue/100
        changeFromGold = changeDue%100

        silverToPlayer = changeFromGold/10%10
        changeFromSilver = changeFromGold%10

        copperToPlayer = changeFromSilver%10


        print("\nYour change:")
        print (str(int(goldToPlayer))+str("gp"))
        print (str(int(silverToPlayer))+str("sp"))
        print (str(int(copperToPlayer))+str("cp"))

    else:
        print("\nInsufficient funds!\n")



    programmeContinue = input(str("\nWould you like to purchase an additional item? y/n "))
    if programmeContinue == "y":
        y = True
    elif programmeContinue == "n":
        print ("\nThank you, come again!\n")
        y = False








