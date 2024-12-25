import aoc
contents = aoc.get_input(2024, 25).strip()
del aoc
# ---

diagrams = contents.split("\n\n")

locks = set()
keys = set()

for d in diagrams:
    lines = d.split("\n")
    if lines[0][0] == "#":
        heights = []
        for x in range(len(lines[0])):
            for y in range(len(lines)):
                if lines[y][x] == ".":
                    break
            heights.append(y - 1)
        locks.add(tuple(heights))


    else:
        heights = []
        for x in range(len(lines[0])):
            for y in range(len(lines)):
                if lines[y][x] == "#":
                    break
            heights.append(y - 1)
        keys.add(tuple([5 - h for h in heights]))

fit = 0
for k in keys:
    for l in locks:
        if any([
            (k[z] + l[z]) >= 6 for z in range(5)
        ]):
            continue
        fit += 1

print(fit)