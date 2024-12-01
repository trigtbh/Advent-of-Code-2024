import aoc
contents = aoc.get_input(2024, 1).strip()
del aoc

# ---

lines = contents.split("\n")
l1 = ([int(l.split(" ")[0]) for l in lines])
l2 = ([int(l.split(" ")[3]) for l in lines])

x = 0
for i in range(len(l1)):
    x += l1[i] * l2.count(l1[i])


print(x)