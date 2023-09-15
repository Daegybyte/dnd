//
//  main.cpp
//  coinManager
//
//  Created by Corg-Sec on 10/7/20.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    bool y = true;
    while (y) {
        
        cout << "\nWould you like to:\n1. Distribute coins to your party?\n2. Purchase an item?\n3. Consolidate your coins?\n\nSelect: ";
        int programmeChoice;
        cin >> programmeChoice;
        //
        //
        //
        //
        
        if (programmeChoice == 1){
            //This is the party loot divider programme
            cout << "\nHow many people are in your party? ";
            int partySize;
            cin >> partySize;
            //coin inputs
            cout << "\n\nHow much loot is being divided?" << endl;
            cout << "\nPlatinum: ";
            int partyPlatinum;
            cin >> partyPlatinum;
            cout << "Gold: ";
            int partyGold;
            cin >> partyGold;
            cout << "Silver: ";
            int partySilver;
            cin >> partySilver;
            cout << "Copper: ";
            int partyCopper;
            cin >> partyCopper;
            
            //platinum
            int platinum = partyPlatinum;
            
            //gross gold
            int grossDividedGold = (partyGold + (platinum*10));
            int gold = grossDividedGold/partySize;
            int goldRemaining = grossDividedGold - (partySize*gold);
            
            //gross silver
            int grossDividedSilver = (partySilver + (goldRemaining*10));
            int silver = grossDividedSilver/partySize;
            int silverRemaining = grossDividedSilver - (partySize*silver);
            
            //gross copper
            int grossDividedCopper = (partyCopper + (silverRemaining*10));
            int copper = grossDividedCopper/partySize;
            int copperRemaining = grossDividedCopper - (partySize*copper);
            
            //outputs
            cout << "\nFor your convenience, platinum has been converted into gold.\n" << endl;
            cout << "Coins per player: "  << endl;
            cout << gold << "gp" << endl;
            cout << silver << "sp" << endl;
            cout << copper << "cp" << endl;
            cout << "Amount remaining in party inventory: " << copperRemaining << "cp\n" << endl;
            
            
            //This is the loot lumper
            //Where the magic happens
            
            int netCopper;
            netCopper = copper%10;
            
            int copperToSilver;
            copperToSilver = copper /10; //using truncation of ints to get copperToSilver
            
            int grossSilver;
            grossSilver =  copperToSilver + silver;
            
            int netSilver;
            netSilver = grossSilver%10;
            
            int silverToGold;
            silverToGold = grossSilver/10;
            
            int netGold;
            netGold = gold + silverToGold;
            
            cout << "Or\n" << endl;
            cout << "Combined coins per player:" << endl;
            cout << netGold << "gp" << endl;
            cout << netSilver << "sp" << endl;
            cout << netCopper << "cp" << endl;
            cout << "Amount remaining in party inventory: " << copperRemaining << "cp\n" << endl;
        }
        //
        //
        //
        //
        if (programmeChoice == 2){
            cout << "\nHow much is the item?" << endl;
            
            cout << "Gold: ";
            int goldPrice;
            cin >> goldPrice;
            goldPrice = goldPrice*100;
            
            cout << "Silver: ";
            int silverPrice;
            cin >> silverPrice;
            silverPrice = silverPrice *10;
            
            cout << "Copper: ";
            int copperPrice;
            cin >> copperPrice;
            
            cout << "Number bought: ";
            int numberBought;
            cin >> numberBought;
            
            cout << "\nHow much money do you have?" << endl;
            
            cout << "Gold: ";
            int goldPaid;
            cin >> goldPaid;
            goldPaid = goldPaid*100;
            
            cout << "Silver: ";
            int silverPaid;
            cin >> silverPaid;
            silverPaid= silverPaid *10;
            
            cout << "Copper: ";
            int copperPaid;
            cin >> copperPaid;
            
            
            
            int combinedPriceInCopper = (goldPrice + silverPrice + copperPrice)*numberBought;
            int combinedPaidInCopper = goldPaid + silverPaid + copperPaid;
            
            if (combinedPaidInCopper < combinedPriceInCopper) {
                cout << "\nInsufficient funds!\n" << endl;
                return 1;
            }
            
            
            int changeDue = combinedPaidInCopper - combinedPriceInCopper;
            
            int goldToPlayer = changeDue/100;
            int changeFromGold = changeDue%100;
            
            int silverToPlayer = changeFromGold/10%10;
            int changeFromSilver = changeFromGold%10;
            
            int copperToPlayer = changeFromSilver%10;
            
            cout << "\nYour new purse total:" << endl;
            cout << goldToPlayer << "gp" << endl;
            cout << silverToPlayer << "sp" <<endl;
            cout << copperToPlayer << "cp\n" << endl;
            //
            //
            //
            //
        }
        if (programmeChoice == 3){
            cout << "\nHow much loot are you adding to your purse?" << endl;
            
            cout << "Gold: ";
            int goldToAddToPurse;
            cin >> goldToAddToPurse;
            goldToAddToPurse = goldToAddToPurse*100;
            
            cout << "Silver: ";
            int silverToAddToPurse;
            cin >> silverToAddToPurse;
            silverToAddToPurse = silverToAddToPurse *10;
            
            cout << "Copper: ";
            int copperToAddToPurse;
            cin >> copperToAddToPurse;
            
            
            cout << "\nHow much loot do you have already in your purse?" << endl;
            
            cout << "Gold: ";
            int currentGoldInPurse;
            cin >> currentGoldInPurse;
            currentGoldInPurse = currentGoldInPurse*100;
            
            cout << "Silver: ";
            int currentSilverInPurse;
            cin >> currentSilverInPurse;
            currentSilverInPurse= currentSilverInPurse *10;
            
            cout << "Copper: ";
            int currentCopperInPurse;
            cin >> currentCopperInPurse;
            
            
            
            int combinedCopperToAdd = (goldToAddToPurse + silverToAddToPurse + copperToAddToPurse)*-1;
            int currentCombinedCopperInPurse = currentGoldInPurse + currentSilverInPurse + currentCopperInPurse;
            
            if (currentCombinedCopperInPurse < combinedCopperToAdd) {
                cout << "\nInsufficient funds!\n" << endl;
                return 1;
            }
            
            
            int updatedCopperInPurse = currentCombinedCopperInPurse - combinedCopperToAdd;
            
            int goldToPurse = updatedCopperInPurse/100;
            int changeFromGold = updatedCopperInPurse%100;
            
            int silverToPurse = changeFromGold/10%10;
            int changeFromSilver = changeFromGold%10;
            
            int copperToPurse = changeFromSilver%10;
            
            
            
            cout << "\nYour new purse total:" << endl;
            cout << goldToPurse << "gp" << endl;
            cout << silverToPurse << "sp" <<endl;
            cout << copperToPurse << "cp\n" << endl;
        }
        cout << "Would you like to start again? y/n: ";
        char programmeContinue = y;
        cin >> programmeContinue;
        if (programmeContinue == 'y'){
            y = true;
        }
        else{
            y = false;
        }
    }
    
    

    return 0;
}
