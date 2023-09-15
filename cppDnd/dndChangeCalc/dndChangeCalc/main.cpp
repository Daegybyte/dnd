//
//  main.cpp
//  dndChangeCalc
//
//  Created by Corg-Sec on 9/19/20.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    
    int partyPlatinum, partyGold, partySilver, partyCopper, partySize;

    cout << "How many people are in your party" << endl;
    cin >> partySize;
    //inputs of the amount of loot to be split by the party
    cout << "\nHow much loot is being divided?" << endl;
    cout << "\nPlatinum: " << endl;
    cin >> partyPlatinum;
    cout << "Gold: " << endl;
    cin >> partyGold;
    cout << "Silver: " << endl;
    cin >> partySilver;
    cout << "Copper: " << endl;
    cin >> partyCopper;
    
    //platinum
    int platinum = partyPlatinum;
    
    //gross gold
    int grossGold = (partyGold + (platinum*10));
    int gold = grossGold/partySize;
    int goldRemainder = grossGold - (partySize*gold);

    //gross silver
    int grossSilver = (partySilver + (goldRemainder*10));
    int silver = grossSilver/partySize;
    int silverRemainder = grossSilver - (partySize*silver);
    
    //gross copper
    int grossCopper = (partyCopper + (silverRemainder*10));
    int copper = grossCopper/partySize;
    int copperRemainder = grossCopper - (partySize*copper);
    
    
    cout << "\nFor your convenience, your platinum has been converted into gold. \n" << endl;
    cout << "Gold per person: " << gold << endl;
    cout << "Silver per person: " << silver << endl;
    cout << "Copper per person: " << copper << endl;
    cout << "\nLeftover copper: " << copperRemainder << endl;

    return 0;
}
