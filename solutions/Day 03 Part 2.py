import aoc
contents = aoc.get_input(2024, 3).strip()
del aoc
# ---
import aoc
contents = aoc.get_input(2024, 3).strip()
del aoc
# ---

tokens = contents.split("mul(")

x = 0

do = True
docopy = do


for token in tokens:


    if "do()" in token:
        ido = token.rindex("do()")
    else:
        ido = None

    if "don't()" in token:
        idont = token.rindex("don't()")
    else:
        idont = None

    


    if ido and not idont:
        do = True

    elif idont and not ido:
        do = False
    elif idont and ido:
        if ido > idont:
            do = True
        else:
            do = False
    

    test = token.split(")")
    if len(test) == 1: 
        docopy = do
        do = docopy
        continue
    items = test[0].split(",")
    if len(items) != 2: 
        docopy = do
        do = docopy
        continue
    p1, p2 = items[0], items[1]
    try:
        p1 = int(p1)
    except: 
        docopy = do
        do = docopy
        continue
    try:
        p2 = int(p2)
    except: 
        docopy = do
        do = docopy
        continue
    
    if p1 < 0 or p2 < 0: continue

    if docopy: x += p1 * p2
    docopy = do
    do = docopy


print(x)