import aoc
contents = aoc.get_input(2024, 19).strip()
del aoc
# ---

tokens, lines = contents.split("\n\n")

lines = lines.split("\n")

tokens = set(tokens.split(", "))

def rec(line):
    if line == "":
        return True
    
    r = False
    for t in tokens:
        if line.startswith(t):
            r = r or rec(line[len(t):])
            if r: return True
    return False

x = 0
for line in lines:
    x += int(rec(line))

print(x)