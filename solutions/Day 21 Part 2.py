import aoc
contents = aoc.get_input(2024, 21).strip()
del aoc
# ---

keypad1 = "789\n456\n123\n 0A".split("\n")
keypad2 = " ^A\n<v>".split("\n")

mapped1 = {}
for y in range(len(keypad1)):
    for x in range(len(keypad1[0])):
        c = keypad1[y][x]
        mapped1[c] = (y, x)

mapped2 = {}
for y in range(len(keypad2)):
    for x in range(len(keypad2[0])):
        c = keypad2[y][x]
        mapped2[c] = (y, x)


def trace1(c1, c2):
    y, x = mapped1[c1]
    ty, tx = mapped1[c2]

    ret = set()

    # vertical first
    s = ""
    valid = True
    while valid and y != ty:
        if y == 3 and x == 0:
            valid = False
        if y > ty:
            s += "^"
            y -= 1
        if y < ty:
            s += "v"
            y += 1
    while valid and x != tx:
        if y == 3 and x == 0:
            valid = False
        if x > tx:
            s += "<"
            x -= 1
        if x < tx:
            s += ">"
            x += 1
    if valid:
        ret.add(s)

    y, x = mapped1[c1]
    # vertical first
    s = ""
    valid = True
    while valid and x != tx:
        if y == 3 and x == 0:
            valid = False
        if x > tx:
            s += "<"
            x -= 1
        if x < tx:
            s += ">"
            x += 1
    while valid and y != ty:
        if y == 3 and x == 0:
            valid = False
        if y > ty:
            s += "^"
            y -= 1
        if y < ty:
            s += "v"
            y += 1
    if valid:
        ret.add(s)

    return ret

def trace2(c1, c2):
    y, x = mapped2[c1]
    ty, tx = mapped2[c2]

    ret = set()

    # vertical first
    s = ""
    valid = True
    while valid and y != ty:
        if y == 0 and x == 0:
            valid = False
        if y > ty:
            s += "^"
            y -= 1
        if y < ty:
            s += "v"
            y += 1
    while valid and x != tx:
        if y == 0 and x == 0:
            valid = False
        if x > tx:
            s += "<"
            x -= 1
        if x < tx:
            s += ">"
            x += 1
    if valid:
        ret.add(s)

    y, x = mapped2[c1]
    # vertical first
    s = ""
    valid = True
    while valid and x != tx:
        if y == 0 and x == 0:
            valid = False
        if x > tx:
            s += "<"
            x -= 1
        if x < tx:
            s += ">"
            x += 1
    while valid and y != ty:
        if y == 0 and x == 0:
            valid = False
        if y > ty:
            s += "^"
            y -= 1
        if y < ty:
            s += "v"
            y += 1
    if valid:
        ret.add(s)

    return ret

charsets1 = {}
for p1 in mapped1:
    for p2 in mapped1:
        if p1 not in charsets1: charsets1[p1] = {}
        charsets1[p1][p2] = trace1(p1, p2)


charsets2 = {}
for p1 in mapped2:
    for p2 in mapped2:
        if p1 not in charsets2: charsets2[p1] = {}
        charsets2[p1][p2] = trace2(p1, p2)


cache = {}

def process(code):
    code = "A" + code
    c = 0
    for i in range(len(code) - 1):
        c1 = code[i]
        c2 = code[i + 1]

        sequences = charsets1[c1][c2]
        available = []
        for s in sequences:
            available.append(recursive("A" + s + "A", 25))
        c += min(available)
    return (c)

def recursive(segment, depth):
    if (segment, depth) in cache:
        return cache[(segment, depth)]
    c = 0


    if depth == 0: return len(segment) - 1

    for i in range(len(segment) - 1):
        c1 = segment[i]
        c2 = segment[i + 1]

        sequences = charsets2[c1][c2]
        available = []
        for s in sequences:
            available.append(recursive("A" + s + "A", depth - 1))
        c += min(available)
    cache[(segment, depth)] = c
    return c


f = 0

for code in contents.split("\n"):
    ml = process(code)
    intrep = int(code.strip("A"))

    f += intrep * ml
    
print(f)