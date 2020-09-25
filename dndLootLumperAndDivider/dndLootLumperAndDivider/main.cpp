//
//  main.cpp
//  dndLootLumperAndDivider
//
//  Created by Corg-Sec on 9/23/20.
//

#include <iostream>
#include "lumper.cpp"
#include "divider.cpp"
using namespace std;

int main(int argc, const char * argv[]) {
    
    bool y = true;
    
    while (y) {
        
//This is the party loot divider programme
    cout << "How many people are in your party? ";
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
    int silverRemainder = grossDividedSilver - (partySize*silver);

//gross copper
    int grossDividedCopper = (partyCopper + (silverRemainder*10));
    int copper = grossDividedCopper/partySize;
    int copperRemaining = grossDividedCopper - (partySize*copper);

//outputs
    cout << "\nFor your convenience, platinum has been converted into gold.\n" << endl;
    cout << "Coins per player: "  << endl;
    cout << gold << "gp" << endl;
    cout << silver << "sp" << endl;
    cout << copper << "cp" << endl;
    cout << "Amount remaining in party inventory: " << copperRemaining << "cp" << endl;


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
        
    cout << "\nOr\n" << endl;
    cout << "Combined coins per player:" << endl;
    cout << netGold << "gp" << endl;
    cout << netSilver << "sp" << endl;
    cout << netCopper << "cp" << endl;
    cout << "Amount remaining in party inventory: " << copperRemaining << "cp\n" << endl;
    
//While loop check
    cout << "Would you like to input more coins? y/n" <<  endl;
    char programmeContinue;
        cin >> programmeContinue;
        if (programmeContinue == 'y') {
            y = true;
        }
        else if (programmeContinue == 'n') {
            cout << "Thank you, come again!" << endl;
            y = false;
            return 1;
        }
    }
    return 0;
}
