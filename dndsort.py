'''Dnd sort by Max Petschack: sorts your dnd file
Usage: Replace demo.txt with your inventory filename (make sure they're in the same folder). Put each item on a new line and
label with [?] at the start of the line where ? is the letter of the item's category. Weapons will sort by damage if formula is given.'''

import re

#Special sorts
def weap_sort(weapons):
    for x in range(len(weapons)):
        damage = re.search('\d*d\d+(\+\d+)?',weapons[x]) #regex for damage formula
        if damage != None:
            rmdflag = 1 if damage.string[damage.start()] == 'd' else 0
            damage = eval(damage.string[damage.start()+rmdflag:damage.end()].replace('d','*'))
        weapons[x] = [damage,weapons[x]]
    weapons = sorted(weapons)[::-1]
    for x in range(len(weapons)):
        weapons[x] = weapons[x][1]
    return weapons

filename = 'demo.txt' #Replace this with your char file 

#Categories
weap = ['WEAPONS/DAMAGE:\n'] #[W]
stat = ['STATS AND STATUSES:\n'] #[S]
gold = ['GOLD/TRADE CREDIT:\n'] #[G]
equip = ['EQUIPMENT:\n'] #[E]
alch = ['ALCHEMY:\n'] #[A]
magic = ['MAGIC:\n'] #[M]
junk = ['JUNK:\n'] #[J]

categories = [['S',stat],['G',gold],['W',weap,weap_sort],['E',equip],['A',alch],['M',magic],['J',junk]]
charfile = open(filename).readlines()

#Read file
print 'Opening File...'
for x in charfile:
    for y in categories:
        if '['+y[0]+']' in x:
            y[1].append(x)

#Sort
print 'Sorting...'
for x in categories:
    if len(x) == 3:
        #Special sort
        x[1][1:] = x[2](x[1][1:])
    else:
        #Regular sort
        x[1][1:] = sorted(x[1][1:])

#Write to file
print 'Writing to file...'
open(filename,'w').write('')
for x in categories:
    x[1].append('\n')
    for y in x[1]:
        open(filename,'a').write(y)

#Add 'NEW ITEMS:' field
open(filename,'a').write('NEW ITEMS:\n')

print 'Done!'
