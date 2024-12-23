import aoc
contents = aoc.get_input(2024, 23).strip()
del aoc
# ---

links = {}
conns = contents.split("\n")
for c in conns:
    c1, c2 = c.split("-")
    if c1 not in links:
        links[c1] = set()
    if c2 not in links:
        links[c2] = set()
    
    links[c1].add(c2)
    links[c2].add(c1)

valid = set()

for p1 in links:
    l = list(links[p1])
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            
            test1 = l[i]
            test2 = l[j]

            chunk = [p1, test1, test2]
            if test1 in links[test2] and any(t[0] == "t" for t in chunk):
                valid.add(tuple(sorted(chunk)))

print(len(valid))