import aoc
contents = aoc.get_input(2024, 8).strip().split("\n")
del aoc
# ---

freqs = {}

for y in range(len(contents)):
    for x in range(len(contents[0])):
        c = contents[y][x]
        if c == ".": continue
        if c not in freqs:
            freqs[c] = set()

        freqs[c].add((y, x))

maxx = len(contents[0]) - 1
maxy = len(contents) - 1


antinodes = set()
for c in freqs:

    points = freqs[c]
    for p in points:
        for p2 in points:
            if p == p2: continue

            y1, x1 = p
            y2, x2 = p2

            i = 0

            while 0 <= (y2 + (y2 - y1) * i) <= maxy and 0 <= (x2 + (x2 - x1) * i) <= maxx:
                antinodes.add((y2 + (y2 - y1) * i, x2 + (x2 - x1) * i))
                i += 1
            
print(len(antinodes))