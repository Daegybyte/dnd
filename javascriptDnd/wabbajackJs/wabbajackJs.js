//D&D Wabbajack by Diego Pisciotta, 2021

/*
How to use:
* Once per short rest

* The wabbajack ignores all resistances, willingness requirements (polymorph),or saving throws unless otherwise specified.
This is because random nature of the Wabbajack essentially functions as the saving throw.
The fact that it did not roll polymorph means you have in a sense beaten a DCnumberOfWabbajackEffects.

* Wabbajack Juice is a potion that magically appears in the player inventory.
The effects are chosen after consumption. But can be a greater restoration potion, but can be aof hill giant strength,
weakness, or of poison resleeved as Bone Hurting Juice. 
The script for  Wabbajack Juice can be found at: https://github.com/Daegybyte/dnd/blob/master/pythonDnd/wabbajack/wabbajackJuice.py
*/


//Arrays to pull from:
var party = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever"];
var person = ["Selsys", "Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"];
var afraidOf = ["Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"];
var polymorph = ["chicken", "goat", "swarm of bees!", "kobold", "cat", "rabbit", "owl", "stein of ale","Bruce Willis", "dire wolf", "yeti", "raven", "polar bear", "T-Rex"];
var buffs = ["enlarge", "reduce", "haste", "freedom of movement", "bardic inspiration"];
var direction = ["squares north", " squares south", "squares east", "squares west"];
var squares = ["one", "two", "three", "four", "five"];

//function to output dice rolls based on xDy format of rolling damage dice x,y
//Roll Dice function
function rollDice(diceToBeRolled,dX){
   let diceOutcome = 0;
   let diceSum = 0;
   for (let i = 0; i < diceToBeRolled; i++){
     diceOutcome = Math.floor(Math.random() * dX)+1;
     diceSum += diceOutcome;
   }
   return diceSum;
 }

var wabbajackSelector = Math.floor(Math.random() * 20) + 1;
var flipCoin = Math.floor(Math.random() * 2);

var rollBallBearings
var rollDistanceNear

var rollPolymorph
var rollBuffs
var rollDirection
var rollSquares
var rollPerson
var rollParty
var rollAfraidOf

//Wabbajack effects:

//Lightning Bolt
if (wabbajackSelector = 1){

}

//Ice Storm
else if(wabbajackSelector = 2){

}

//Heal
else if(wabbajackSelector = 3){

}

//Make it rain
else if (wabbajackSelector = 4){

}

//Polymorph
else if (wabbajackSelector = 5){

}

//Invisibility
else if(wabbajackSelector = 6){

}

//Summon Kobold
else if(wabbajackSelector = 7){

}

//Prone
else if (wabbajackSelector = 8){

}

//Wabbajack Juice
else if (wabbajackSelector = 9){

}
//fear
else if (wabbajackSelector = 10){

}

//Exhaustion
else if(wabbajackSelector = 11){

}

//Ballbearings
else if(wabbajackSelector = 12){

}

//Absorb HP
else if(wabbajackSelector= 13){

}

//Buffs
else if(wabbajackSelector = 14){

}

//Cheese Storm
else if(wabbajackSelector = 15){

}

//Random Damage
else if(wabbajackSelector = 16){

}

//Explosion
else if(wabbajackSelector = 17){

}

//Lucky
else if (wabbajackSelector = 18){

}

//Spectral Shield
else if(wabbajackSelector = 19){

}

//Fireball
else if(wabbajackSelector = 20){
    
}