import aoc
contents = aoc.get_input(2024, 16).strip()
del aoc
# ---

grid = contents.split("\n")
walls = set()

junctions = dict()


class Junction:
    def __init__(self, y, x):
        self.y = y
        self.x = x

        self.connections = {}
        self.cost = float("inf")

        self.endfound = False

    def __repr__(self):
        return f"J({self.y}, {self.x} - min: {self.cost})"
    

start = ()
end = ()

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] != "#":
            left = grid[y][x - 1] != "#"
            right = grid[y][x + 1] != "#"
            up = grid[y - 1][x] != "#"
            down = grid[y + 1][x] != "#"
        
            if not (left and right and not up and not down) and not (up and down and not left and not right):
                junctions[(y, x)] = Junction(y, x)

        if grid[y][x] == "S": start = (y, x)
        if grid[y][x] == "E": end = (y, x)
        

for t in junctions:
    j = junctions[t]
    y = j.y
    x = j.x


    cy = j.y + 1
    while True:
        if grid[cy][x] == "#": break
        if (cy, x) in junctions:
            j.connections[junctions[(cy, x)]] = (abs(y - cy), 3)
            # break

        cy += 1

    cy = j.y - 1
    while True:
        if grid[cy][x] == "#": break
        if (cy, x) in junctions:
            j.connections[junctions[(cy, x)]] = (abs(y - cy), 1)
            # break

        cy -= 1

    cx = j.x + 1
    while True:
        if grid[y][cx] == "#": break
        if (y, cx) in junctions:
            j.connections[junctions[(y, cx)]] = (abs(x - cx), 2)
            # break

        cx += 1

    cx = j.x - 1
    while True:
        if grid[y][cx] == "#": break
        if (y, cx) in junctions:
            j.connections[junctions[(y, cx)]] = (abs(x - cx), 4)
            # break


        cx -= 1

    j.connections = {k: v for k, v in sorted(j.connections.items(), key=lambda item: item[1][0])}

global vblank
vblank = set()



def rec(pos, cost, direction, visited, depth):
    # print(pos)
    global vblank
    if pos == junctions[end]:
        if cost < pos.cost:
            for p in vblank:
                p.endfound = False
            vblank = visited.copy()
        elif cost == pos.cost:
            vblank |= visited.copy()
        for p in vblank:
            p.endfound = True

        # return

    if cost > pos.cost:
        return
    elif cost == pos.cost:
        if pos.endfound:
            vblank |= visited
            for p in vblank:
                p.endfound = True
        return
    if depth == 998: return
    pos.cost = cost

    for potential in pos.connections:
        if potential not in visited:
            length, newdir = pos.connections[potential]
            nc = cost + length
            if newdir != direction: 
                nc += 1000

            if nc <= potential.cost: 
                visited.add(potential)
                rec(potential, nc, newdir, visited, depth + 1)
                visited.remove(potential)

rec(junctions[start], 0, 2, set(), 0)

# print(junctions[end].cost)
# print(vblank)

vblank.add(junctions[start])

points = set([
    (p.y, p.x) for p in vblank
])

# print(sorted(points))


path_junctions = {
    junctions[p] for p in points
}

points = set()

for j1 in path_junctions:
    valid = set(j1.connections.keys()).intersection(path_junctions)
    for j2 in valid:
        # print(f"{j1} -> {j2}")

        for dy in range(j2.y - j1.y + 1):
            for dx in range(j2.x - j1.x + 1):
                points.add(
                    (j1.y + dy, j1.x + dx)
                )
                # input((j1.y + dy, j1.x + dx))

# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == "#":
#             print("#", end="")
#         elif (y, x) in points:
#             print(".", end="")
#         else:
#             print(" ", end="")
#     print()

print(len(points))
