import aoc
contents = aoc.get_input(2024, 13).strip()
del aoc
# ---

machines = contents.split("\n\n")

c = 0

for machine in machines:
    b1, b2, target = machine.split("\n")

    target = list(map(int, [t.split("=")[1] for t in target.split(": ")[1].split(", ")]))
    
    aup = list(map(int, [t.split("+")[1] for t in b1.split(": ")[1].split(", ")]))
    bup = list(map(int, [t.split("+")[1] for t in b2.split(": ")[1].split(", ")]))
    

    mincost = 999999999
    found = False
    for a in range(101):
        for b in range(101):
            x = a * aup[0] + b * bup[0]
            y = a * aup[1] + b * bup[1]
            if [x, y] == target:
                found = True
                if (3 * a + b) < mincost:
                    mincost = (3 * a + b)
    if found: c += mincost

print(c)