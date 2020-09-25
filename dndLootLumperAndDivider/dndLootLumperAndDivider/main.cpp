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

    
////    This is the party loot divider programme
//    int partyPlatinum, partyGold, partySilver, partyCopper, partySize;
//
//    cout << "How many people are in your party" << endl;
//    cin >> partySize;
//    //inputs of the amount of loot to be split by the party
//    cout << "\nHow much loot is being divided?" << endl;
//    cout << "\nPlatinum: " << endl;
//    cin >> partyPlatinum;
//    cout << "Gold: " << endl;
//    cin >> partyGold;
//    cout << "Silver: " << endl;
//    cin >> partySilver;
//    cout << "Copper: " << endl;
//    cin >> partyCopper;
//
//    //platinum
//    int platinum = partyPlatinum;
//
//    //gross gold
//    int grossGold = (partyGold + (platinum*10));
//    int gold = grossGold/partySize;
//    int goldRemainder = grossGold - (partySize*gold);
//
//    //gross silver
//    int grossSilver = (partySilver + (goldRemainder*10));
//    int silver = grossSilver/partySize;
//    int silverRemainder = grossSilver - (partySize*silver);
//
//    //gross copper
//    int grossCopper = (partyCopper + (silverRemainder*10));
//    int copper = grossCopper/partySize;
//    int copperRemainder = grossCopper - (partySize*copper);
//
//
//    cout << "\nFor your convenience, your platinum has been converted into gold. \n" << endl;
//    cout << "Gold per person: " << gold << endl;
//    cout << "Silver per person: " << silver << endl;
//    cout << "Copper per person: " << copper << endl;
//    cout << "|nLeftover copper: " << copperRemainder << endl;
    
    
    
    
//    This is the loot lumper
    
//    int goldInput=0, copperRemaining=0, grossSilver=0, netGold=0;
//
//    cout << "Please enter the number of each coin:" << endl;
//    cout << "Gold:" << endl;
//    int goldInput
//    cin >> goldInput;
//    cout << "Silver:" << endl;
//    int silverInput
//    cin >> silverInput;
//    cout << "Copper:" << endl;
//    int copperInput;
//    cin >> copperInput;
//
//    //Where the magic happens
//
//    copperRemaining = copperInput%10;
//
//    int copperToSilver;
//    copperToSilver = copperInput /10; //using truncation of ints to get copperToSilver
//
//    grossSilver =  copperToSilver + (silverInput);
//
//    int netSilver;
//    netSilver = grossSilver%10;
//
//    int silverToGold;
//    silverToGold = grossSilver/10;
//
//    netGold = goldInput + silverToGold;
//
//
//    cout << "\nCombined coins:" << endl;
//    cout << netGold << "gp" << endl;
//    cout << netSilver << "sp" << endl;
//    cout << copperRemaining << "cp" << endl;
    
    
    return 0;
}
