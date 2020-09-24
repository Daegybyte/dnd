//
//  main.cpp
//  dndCoinLumper
//
//  Created by Corg-Sec on 9/21/20.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {

    int copperInput=0, silverInput=0, goldInput=0, copperRemaining=0, grossSilver=0, netGold=0;
    
    cout << "Please enter the number of each coin:" << endl;
    cout << "Gold:" << endl;
    cin >> goldInput;
    cout << "Silver:" << endl;
    cin >> silverInput;
    cout << "Copper:" << endl;
    cin >> copperInput;
    
    //Where the magic happens
    
    copperRemaining = copperInput%10;
    
    int copperToSilver;
    copperToSilver = copperInput /10; //using truncation of ints to get copperToSilver

    grossSilver =  copperToSilver + (silverInput);
    
    int netSilver;
    netSilver = grossSilver%10;
    
    int silverToGold;
    silverToGold = grossSilver/10;

    netGold = goldInput + silverToGold;
    
    
    cout << "\nCombined coins:" << endl;
    cout << netGold << "gp" << endl;
    cout << netSilver << "sp" << endl;
    cout << copperRemaining << "cp" << endl;
    
    return 0;
}
