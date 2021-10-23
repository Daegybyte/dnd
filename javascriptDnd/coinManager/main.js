"use strict";

btnCalculate.addEventListener("click", consolidateCoins);
function consolidateCoins() {

    let gold_ = parseInt(gold.value) * 100;
    let silver_ = parseInt(silver.value) * 10;
    let copper_ = parseInt(copper.value);

    errorCheckCoin(gold_);

    let coins = parseInt(gold_ + silver_ + copper_);

    gold_ = parseInt(coins / 100);
    let changeFomGold = parseInt(coins % 100);

    silver_ = parseInt(changeFomGold / 10 % 10);
    let changeFromSilver = parseInt(changeFomGold % 10);

    copper_ = parseInt(changeFromSilver % 10);

    document.getElementById("goldToPlayer").value = gold_;
    document.getElementById("silverToPlayer").value = silver_;
    document.getElementById("copperToPlayer").value = copper_;
}

function errorCheckCoin(coin) {
    let gold = document.getElementById("gold");
    if(coin.name === gold){
        console.log("here")

        let name = document.getElementById("gold".name)
        if (isNaN(coin.value)) {
            console.log("here");
            alert(name + " cannot be empty!");
        }
    }
}

