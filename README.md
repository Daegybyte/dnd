# Dungeons & Dragons related programmes

## Wabbajack
### An item ported to D&D from Elder Scrolls, the wabbajack brings fun and chaos to any campaign
- wabbajack.py runs the main programme for the item. It rolls and decides the fates of each player. Sometimes for good, sometimes<br />for the funny.
-wabbajackJuice.py is a secondary programme used for if a player has decided to risk drinking the potion (wabbajack juice) in their inventory.
- Buffs is a basic programme to randomly select buffs. It started as a practice programme, but stays in the collection because it<br />might somehow be useful later.

## coinManager
- user input 1,2,3 to decide which programme from below to run.

### dndLootLumperAndDivider
- Is a programme made from combining dndChangeCalc and dndCoinLumper programmes.
- Takes the number of members in a party, evenly distributes loot, and then optimises that disbursal. User can decide which they prefer to add to their purse.
- leftover coins are marked to be returned to the party purse.

### itemChangeGiver
- Takes gold, silver, and copper as inputs for item price and price paid. Then outputs the change the player is owed in descending value of coin gold, silver, copper.

### purseUpdaterDnd
- Uses mostly the same code as itemChangeGiver, but multiplies the amount of loot to add to purse by -1 to then add the difference.

<br />
## cppDnd
### A collection of some of the above programmes written into C++. Added when I see fit.