'''Dnd sort by Max Petschack: sorts your dnd file
Usage: Replace demo.txt with your inventory filename (make sure they're in the same folder). Put each item on a new line and
label with [?] at the start of the line where ? is the letter of the item's category. Weapons will sort by damage if formula is given.'''

import re

#Special sorts
def weap_sort(weapons):
    for x in range(len(weapons)):
        damage = re.search('\d*d\d+(\+\d+)?',weapons[x])
        if damage != None:
            rmdflag = 1 if damage.string[damage.start()] == 'd' else 0 #Remove d if it's the first char
            damage = eval(damage.string[damage.start()+rmdflag:damage.end()].replace('d','*')) #Turn damage formula into equation
        weapons[x] = [damage,weapons[x]] #Tag weapon with it's max damage
    weapons = sorted(weapons)[::-1]
    for x in range(len(weapons)):
        weapons[x] = weapons[x][1]
    return weapons

def gold_sort(gold):
    global rates
    for x in range(len(gold)):
        value = re.findall('\d+[csepg]p?',gold[x])
        if len(value) > 0:
            #Got some coin strings, figure out how valuble they are
            total = 0
            coinregxs = ['\d+cp?','\d+cp?','\d+ep?','\d+gp?','\d+pp?']
            for k in value:
                for y in range(5):
                    instring = re.search(coinregxs[y],k)
                    if instring != None:
                        total += int(re.sub('[csegpCSEGP]','',instring.string))*rates[y]
            gold[x] = [total,gold[x]]
        else:
            gold[x] = [None,gold[x]]
    gold = sorted(gold)[::-1]
    for x in range(len(gold)):
        gold[x] = gold[x][1]
    return gold

filename = 'demo.txt' #Replace this with your char file 

#Categories
weap = ['WEAPONS/DAMAGE:\n'] #[W]
stat = ['STATS AND STATUSES:\n'] #[S]
gold = ['GOLD/VALUBLE THINGS:\n'] #[G]
equip = ['EQUIPMENT:\n'] #[E]
alch = ['ALCHEMY:\n'] #[A]
magic = ['MAGIC/SPELLS:\n'] #[M]
junk = ['JUNK/MISC:\n'] #[J]

#Value of each currency denomenation in copper. Defaults to dnd5e.
#Order is copper, silver, electrum, gold, platinum.

rates = [1,10,50,100,1000]

categories = [['S',stat],['G',gold,gold_sort],['W',weap,weap_sort],['E',equip],['A',alch],['M',magic],['J',junk]]
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
