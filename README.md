# dnd-sort

## A sorting tool for text based dnd inventories

### Features:

* Sorts items into categories
* Sorts categories alphabetically
* Sorts weapons by max damage
* More special sorts coming in the future

### Usage:

Replace demo.txt with your inventory filename (make sure they're in the same folder). Put each item on a new line and
label with [?] at the start of the line where ? is the letter of the item's category. Weapons will sort by damage if formula is given. Formulas should look like '2d4+1' where the initial number before the d and the trailing addition are optional.

### Valid categories:

* Weapons [W]
* Stats and statuses [S]
* Gold/trade credit [G]
* Equipment [E]
* Alchemy [A]
* Magic [M]
* Junk [J]