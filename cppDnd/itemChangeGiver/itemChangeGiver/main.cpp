//
//  main.cpp
//  itemChangeGiver
//
//  Created by Corg-Sec on 10/1/20.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    
    bool y = true;
    while (y) {
    
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
        
        char programmeContinue = y;
        cout << "Would you like to purchase an additional item? y/n\n"<<endl;
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
