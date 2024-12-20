import aoc
contents = aoc.get_input(2024, 20).strip()
del aoc
# ---

maxl = contents.count(".") + 1

grid = contents.split("\n")

start = None
end = None



valid = {}
valid2 = {}
visited = {}
visited2 = {}

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "S":
            start = (y, x)
        elif grid[y][x] == "E":
            end = (y, x)
        
        if grid[y][x] != "#":
            valid[(y, x)] = float("inf")
            valid2[(y, x)] = float("inf")
            





valid[end] = 0
valid2[start] = 0


while len(valid) > 0:
    point = min(valid.keys(), key=lambda point: valid[point])

    py, px = point
    visited[point] = valid[point]
    del valid[point]

    for (ny, nx) in {
        (py - 1, px),
        (py + 1, px),
        (py, px - 1),
        (py, px + 1),
    }:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            if grid[ny][nx] != "#" and (ny, nx) in valid:
                temp = visited[point] + 1
                if temp < valid[(ny, nx)]:
                    valid[(ny, nx)] = temp

while len(valid2) > 0:
    point = min(valid2.keys(), key=lambda point: valid2[point])

    py, px = point
    visited2[point] = valid2[point]
    del valid2[point]

    for (ny, nx) in {
        (py - 1, px),
        (py + 1, px),
        (py, px - 1),
        (py, px + 1),
    }:
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
            if grid[ny][nx] != "#" and (ny, nx) in valid2:
                temp = visited2[point] + 1
                if temp < valid2[(ny, nx)]:
                    valid2[(ny, nx)] = temp


global costs
costs = {}

global cache
cache = {}


paths = [
    (start, set(), False, 0)
]

djk = visited

threshold = 100


def scan(py, px):
    s  = set()
    for dy in range(-20, 21):
        for dx in range(-20, 21):


            ny = py + dy
            nx = px + dx

            if abs(dy) + abs(dx) <= 20:
                s.add((ny, nx, abs(dy) + abs(dx)))


            # if abs(y) + abs(x) <= 20:
            #     s.add((py + y, px + x, abs(y - py) + abs(x - px)))

    return s


for py in range(len(grid)):
    for px in range(len(grid[0])):
        if (py, px) not in visited2: continue
        c1 = visited2[(py, px)]

        if maxl - c1 < threshold: continue

        for (ny, nx, nc) in scan(py, px):
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
                if grid[ny][nx] != "#":
                    c2 = visited[(ny, nx)]
                    diff = maxl - (c1 + c2 + nc)
                    if diff >= threshold:
                        if diff not in costs:
                            costs[diff] = 0
                        costs[diff] += 1


# print(sorted(costs))
# print(sorted(costs.items()))

print(sum(list(costs.values())))
# print(sorted(costs.items(), key=lambda x: x[1], reverse=True))