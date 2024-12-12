import aoc
contents = aoc.get_input(2024, 12).strip()
del aoc
# ---

board = contents.split("\n")

points = set()
for y in range(len(board)):
    for x in range(len(board[0])):
        points.add((y, x))

prices = 0



while len(points) > 0:
    subsection = set()
    point = points.pop()

    char = board[point[0]][point[1]]
    scan = set()
    scan.add(point)
    subsection.add(point)

    while len(scan) > 0:
        y, x = scan.pop()

        to_add = set()

        for (ny, nx) in {
            (y - 1, x),
            (y + 1, x),
            (y, x - 1),
            (y, x + 1)
        }.intersection(points):
            if board[ny][nx] == char:
                to_add.add((ny, nx))
    
        to_add -= subsection
        subsection.add((y, x))
        scan |= to_add
    
    points -= subsection

    area = len(subsection)


    perimeter = 0
    tagged = set()
    for y in range(-1, len(board) + 1):
        s = set(p[1] for p in subsection if p[0] == y)

        perimeter += len(s - tagged)
        perimeter += len(tagged - s)

        tagged = s
    
    tagged = set()
    for x in range(-1, len(board[0]) + 1):
        s = set(p[0] for p in subsection if p[1] == x)

        perimeter += len(s - tagged)
        perimeter += len(tagged - s)

        tagged = s

    prices += area * perimeter

print(prices)


