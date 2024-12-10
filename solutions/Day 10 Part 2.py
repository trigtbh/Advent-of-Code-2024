import aoc
contents = aoc.get_input(2024, 10).strip().split("\n")
del aoc
# ---


def rec(y, x, n):
    if n == 9:
        if int(contents[y][x]) == n:
            return 1
        return 0
    
    
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
                ret += rec(ny, nx, n + 1)

    return ret

t = 0
for y in range(len(contents)):
    for x in range(len(contents[0])):
        if int(contents[y][x]) == 0:
            points = set()
            v = rec(y, x, 0)
            # v = len(points)
            # print(v)
            # input()
            t += v

print(t)