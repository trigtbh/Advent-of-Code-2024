import aoc
contents = aoc.get_input(2024, 1).strip()
del aoc

# ---

lines = contents.split("\n")
l1 = sorted([int(l.split(" ")[0]) for l in lines])
l2 = sorted([int(l.split(" ")[3]) for l in lines])

x = 0
for i in range(len(l1)):
    x += abs(l1[i] - l2[i])

print(x)