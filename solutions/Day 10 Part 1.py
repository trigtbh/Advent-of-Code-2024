import aoc
contents = aoc.get_input(2024, 10).strip().split("\n")
del aoc
# ---


def rec(y, x, n, points):
    if n == 9:
        if int(contents[y][x]) == n:
            points.add((y, x))
        return
    
    
    ret = 0

    for point in {
        (y - 1, x),
        (y + 1, x),
        (y, x - 1),
        (y, x + 1)
    }:
        ny, nx = point
        if (0 <= ny < len(contents)) and (0 <= nx < len(contents[0])):
            if int(contents[ny][nx]) == (n + 1):
                rec(ny, nx, n + 1, points)


t = 0
for y in range(len(contents)):
    for x in range(len(contents[0])):
        if int(contents[y][x]) == 0:
            points = set()
            rec(y, x, 0, points)
            v = len(points)
            t += v

print(t)