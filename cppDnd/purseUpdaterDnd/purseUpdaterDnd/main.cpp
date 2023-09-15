//
//  main.cpp
//  purseUpdaterDnd
//
//  Created by Corg-Sec on 10/5/20.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    bool y = true;
    while (y) {
    
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
        
        char programmeContinue = y;
        cout << "\nWould you like to add more loot? y/n\n"<<endl;
        cin >> programmeContinue;
        if (programmeContinue == 'y'){
            y = true;
        }
        if (programmeContinue == 'n'){
            cout << "\nThank you, come again!\n" << endl;
            y = false;
            
        }
        
    }
    return 0;
}
