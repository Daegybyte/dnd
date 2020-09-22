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
    
    cout << "Please enter your coin values:" << endl;
    cout << "Gold:" << endl;
    cin >> goldInput;
    cout << "Silver:" << endl;
    cin >> silverInput;
    cout << "Copper:" << endl;
    cin >> copperInput;
    
    
    lumpedCopper = copperInput%10; //find the remaining value of copper
    
    lumpedSilver =  ((copperInput - (copperInput%10))/10) + (silverInput - silverInput%10); //for every 10 copper, add 1 silver
    
    lumpedGold = ((lumpedSilver/10) + goldInput);
    
    cout << "\nLumped coins:" << endl;
    cout << lumpedGold << "gp" << endl;
    cout << lumpedSilver << "sp" << endl;
    cout << lumpedCopper << "cp" << endl;
    
//    lumpedSilver ((copperInput - (copperInput%10))/10) + (silverInput - silverInput%10);
    
    return 0;
}
