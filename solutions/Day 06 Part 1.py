import aoc
contents = aoc.get_input(2024, 6).strip()
del aoc
# ---

rows = contents.split("\n")

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

print(len(spots))