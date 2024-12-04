import aoc
contents = aoc.get_input(2024, 4).strip().split()
del aoc
# ---


def rec2(y, x, dy, dx, target):
    if target == "": 
        
        return 1
    y += dy
    x += dx


    f = 0
    if (0 <= y < len(contents) and 0 <= x < len(contents[0])):
        if contents[y][x] == target[0]:
            f += rec2(y, x, dy, dx, target[1:])

    return f


def rec(y, x, target):
    f = 0

    for dy, dx in {
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    }:
        ny = y + dy
        nx = x + dx

        if (0 <= ny < len(contents) and 0 <= nx < len(contents[0])):
            if contents[ny][nx] == target[0]:
                f += rec2(ny, nx, dy, dx, target[1:])

    return f


x = 0
for iy in range(len(contents)):
    for ix in range(len(contents[0])):
        if contents[iy][ix] == "X":
            x += rec(iy, ix, "MAS")
            
print(x)