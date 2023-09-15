"use strict";


setZero();
let btnCalculate = document.getElementById("btnCalculate");
btnCalculate.addEventListener("click", consolidateCoins);

function consolidateCoins() {
    let gold_ = parseInt(gold.value) * 100;
    let silver_ = parseInt(silver.value) * 10;
    let copper_ = parseInt(copper.value);
    let purseGold_ = parseInt(goldInPurse.value) * 100;
    let purseSilver_ = parseInt(silverInPurse.value) * 10;
    let purseCopper_ = parseInt(copperInPurse.value);

    let purseCoins = parseInt(purseGold_ + purseSilver_ + purseCopper_);
    let coins = parseInt(gold_ + silver_ + copper_ + purseCoins);

    gold_ = parseInt(coins / 100);
    let changeFomGold = parseInt(coins % 100);

    silver_ = parseInt(changeFomGold / 10 % 10);
    let changeFromSilver = parseInt(changeFomGold % 10);

    copper_ = parseInt(changeFromSilver % 10);

    document.getElementById("goldToPlayer").value = gold_;
    document.getElementById("silverToPlayer").value = silver_;
    document.getElementById("copperToPlayer").value = copper_;
}

function setZero(){
    document.getElementById('gold').value = Number(0);
    document.getElementById('silver').value = Number(0);
    document.getElementById('copper').value = Number(0);

    document.getElementById('goldToPlayer').value = Number(0);
    document.getElementById('silverToPlayer').value = Number(0);
    document.getElementById('copperToPlayer').value = Number(0);

    document.getElementById('goldInPurse').value = Number(0);
    document.getElementById('silverInPurse').value = Number(0);
    document.getElementById('copperInPurse').value = Number(0);
}

