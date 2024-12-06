import aoc
contents = aoc.get_input(2024, 6).strip()
del aoc
# ---

rows = contents.split("\n")

rows = [[c for c in row] for row in rows]

pos = contents.replace("\n", "").index("^")
y = pos // len(rows[0])
x = pos % len(rows[0])


direction = 0

spots = set()

while (0 <= y < len(rows)) and (0 <= x < len(rows[0])):
    spots.add((y, x))
    ny = y
    nx = x
    if direction == 0:
        ny -= 1
    if direction == 1:
        nx += 1
    if direction == 2:
        ny += 1
    if direction == 3:
        nx -= 1
    
    if (not ((0 <= ny < len(rows)) and (0 <= nx < len(rows[0])))):
        break

    if rows[ny][nx] == "#":
        direction = (direction + 1) % 4
    else:
        y = ny
        x = nx

loopable = 0



i = 0
for available in spots:
    ay, ax = available
    
    rows[ay][ax] = "#"

    y = pos // len(rows[0])
    x = pos % len(rows[0])

    testing = set()

    direction = 0

    while (0 <= y < len(rows)) and (0 <= x < len(rows[0])):

        if (y, x, direction) in testing:
            loopable += 1
            break

        testing.add((y, x, direction))
        ny = y
        nx = x
        if direction == 0:
            ny -= 1
        if direction == 1:
            nx += 1
        if direction == 2:
            ny += 1
        if direction == 3:
            nx -= 1
        
        if (not ((0 <= ny < len(rows)) and (0 <= nx < len(rows[0])))):
            break

        if rows[ny][nx] == "#":
            direction = (direction + 1) % 4
        else:
            y = ny
            x = nx

    rows[ay][ax] = "."

print(loopable)