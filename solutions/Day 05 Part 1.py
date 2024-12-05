import aoc
contents = aoc.get_input(2024, 5).strip()
del aoc
# ---

s1, s2 = contents.split("\n\n")
pairs = {}
for line in s1.split("\n"):
    x, y = line.split("|")
    if int(x) not in pairs:
        pairs[int(x)] = set()
    pairs[int(x)].add(int(y))

total = 0
for line in s2.split("\n"):
    i = 0
    indexes = {}
    for item in line.split(","):
        item = int(item)
        indexes[item] = i
        i += 1
    
    
    good = True
    
    for item in indexes:
        if item not in pairs: continue
        tolook = pairs[item].intersection(indexes.keys())

        for item2 in tolook:
            if indexes[item] > indexes[item2]:
                good = False
                break
        if not good: 
            break

    if good:
        total += int(line.split(",")[i // 2])

print(total)