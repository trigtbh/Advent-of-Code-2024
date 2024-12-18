import aoc
contents = aoc.get_input(2024, 18).strip()
del aoc
# ---

walls = list(

    tuple(map(int, l.split(",")[::-1]))
    for l in contents.split("\n")

)

walls = set(walls[:1024])

grid = contents.split("\n")

valid = {}
visited = {}

length = 70

for y in range(length + 1):
    for x in range(length + 1):
        if (y, x) not in walls:
            valid[(y, x)] = float("inf")

valid[(0, 0)] = 0
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
        if 0 <= ny <= length and 0 <= nx <= length:
            if (ny, nx) not in walls and (ny, nx) in valid:
                temp = visited[point] + 1
                if temp < valid[(ny, nx)]:
                    valid[(ny, nx)] = temp

    # print(sorted(valid.items(), key = ;a))

print(visited[(70, 70)])