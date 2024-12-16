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
        self.mincost = float("inf")
    def __repr__(self):
        return f"J({self.y}, {self.x} - min: {self.mincost})"

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

def rec(pos, cost, direction, visited, depth):
    # print(pos)
    if cost >= pos.mincost:
        return
    if depth == 998: return
    pos.mincost = cost

    for potential in pos.connections:
        if potential not in visited:
            length, newdir = pos.connections[potential]
            nc = cost + length
            if newdir != direction: 
                nc += 1000

            if nc < potential.mincost: 
                visited.add(potential)
                rec(potential, nc, newdir, visited, depth + 1)
                visited.remove(potential)

rec(junctions[start], 0, 2, set(), 0)

print(junctions[end].mincost)