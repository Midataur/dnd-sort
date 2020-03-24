# dnd-sort

## A Python 2.7 tool for sorting text based dnd inventories 

### Features:

* Sorts items into categories
* Sorts categories alphabetically
* Sorts weapons by max damage
* More special sorts coming in the future

### Usage:

Replace demo.txt with your inventory filename (make sure they're in the same folder). Put each item on a new line and
label with [?] at the start of the line where ? is the letter of the item's category.

### Valid categories:

* Weapons/Damage [W]
* Stats and statuses [S]
* Gold/Trade credit [G]
* Equipment [E]
* Alchemy [A]
* Magic/Spells [M]
* Junk/Misc [J]

#### Special sorts:

* Weapons will sort by damage if formula is given. Formulas should look like '2d4+1' where the initial number before the d and the trailing addition are optional.
* Gold and valuable items will sort by value if values are given in the format '423gp 56sp 2cp' where the p is optional. Supported currency types are cp (copper), sp (silver), ep (electrum), gp (gold) and pp (platinum). Exchange rates are dnd5e by default. 
* Spells are sorted by level. Level can be given in 1 of 2 formats: '(Level 12)' where the case doesn't matter for the L or '(Lv 4)' where the case doesn't matter for the L and the space is optional.
