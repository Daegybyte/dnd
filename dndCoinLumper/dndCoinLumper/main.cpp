//
//  main.cpp
//  dndCoinLumper
//
//  Created by Corg-Sec on 9/21/20.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {

    int copperInput=0, silverInput=0, goldInput=0, lumpedCopper=0, lumpedSilver=0, lumpedGold=0;
    
    cout << "Please enter the number of each coin:" << endl;
    cout << "Gold:" << endl;
    cin >> goldInput;
    cout << "Silver:" << endl;
    cin >> silverInput;
    cout << "Copper:" << endl;
    cin >> copperInput;
    
    //Where the magic happens
    
    lumpedCopper = copperInput%10;
    
    int copperToSilver;
    copperToSilver = copperInput /10;

    lumpedSilver =  copperToSilver + (silverInput - (silverInput%10));
    
    int silverToGold;
    silverToGold = lumpedSilver/10;
    
    int totalSilver;
    totalSilver = (silverInput%10 + copperToSilver%10)%10; 


    lumpedGold = goldInput + silverToGold;
    
    
    cout << "\nCombined coins:" << endl;
    cout << lumpedGold << "gp" << endl;
    cout << totalSilver << "sp" << endl;
    cout << lumpedCopper << "cp" << endl;
    
    return 0;
}
