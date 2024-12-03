import aoc
contents = aoc.get_input(2024, 3).strip()
del aoc
# ---

tokens = contents.split("mul(")

x = 0
for token in tokens:
    test = token.split(")")
    if len(test) == 1: continue
    items = test[0].split(",")
    if len(items) != 2: continue
    p1, p2 = items[0], items[1]
    try:
        p1 = int(p1)
    except: continue
    try:
        p2 = int(p2)
    except: continue
    
    if p1 < 0 or p2 < 0: continue

    x += p1 * p2
print(x)