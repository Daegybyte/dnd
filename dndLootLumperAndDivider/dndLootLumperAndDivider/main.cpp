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

    
//    This is the party loot divider programme
    cout << "How many people are in your party" << endl;
    int partySize;
    cin >> partySize;
    //coin inputs
    cout << "\nHow much loot is being divided?" << endl;
    cout << "\nPlatinum: " << endl;
    int partyPlatinum;
    cin >> partyPlatinum;
    cout << "Gold: " << endl;
    int partyGold;
    cin >> partyGold;
    cout << "Silver: " << endl;
    int partySilver;
    cin >> partySilver;
    cout << "Copper: " << endl;
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
    cout << "\nFor your convenience, your platinum has been converted into gold. \n" << endl;
    cout << "Gold per person: " << gold << endl;
    cout << "Silver per person: " << silver << endl;
    cout << "Copper per person: " << copper << endl;
    cout << "\nLeftover copper: " << copperRemaining << endl;


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


    cout << "\nCombined coins:" << endl;
    cout << netGold << "gp" << endl;
    cout << netSilver << "sp" << endl;
    cout << netCopper << "cp" << endl;
    cout << "\nLeftover copper: " << copperRemaining << endl;
    
    
    return 0;
}
