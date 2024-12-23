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

maxclique = set()

for p1 in links:
    l = list(links[p1])
    clique = set()
    clique.add(p1)
    for p2 in l:
        valid = True
        for item in clique:
            if p2 not in links[item]:
                valid = False
                break
        if valid:
            clique.add(p2)
    
    if len(clique) > len(maxclique):
        maxclique = clique
print(",".join(sorted(list(maxclique))))