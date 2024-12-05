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

    if not good:
        c = i
        # total += int(line.split(",")[i // 2])
        
        line = list(map(int, line.split(",")))
        i = len(line) - 2
        while i >= 0:
            for j in range(i + 1, len(line)):
                item1 = line[i]
                item2 = line[j]
                if item2 not in pairs: continue
                if item1 in pairs[item2]:
                    line.insert(i, line.pop(j))
                    i += 1
                # print(f"{i} -> {item1}; {j} -> {item2}")
                # print(line)
                # input()
            i -= 1

        total += line[c // 2]

print(total)