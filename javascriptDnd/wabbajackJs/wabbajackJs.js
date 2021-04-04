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
 var AfraidOf = ["Nestor", "Rafe", "Friday","Theodor","Sever", "the nearest enemy", "the farthest enemy"];
 var polymorph = ["chicken", "goat", "swarm of bees!", "kobold", "cat", "rabbit", "owl", "stein of ale","Bruce Willis", "dire wolf", "yeti", "raven", "polar bear", "T-Rex"];
 var buffs = ["enlarge", "reduce", "haste", "freedom of movement", "bardic inspiration"];
 var direction = ["squares north", " squares south", "squares east", "squares west"];
 var squares = ["one", "two", "three", "four", "five"];


