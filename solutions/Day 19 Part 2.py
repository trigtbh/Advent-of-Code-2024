import aoc
contents = aoc.get_input(2024, 19).strip()
del aoc
# ---

tokens, lines = contents.split("\n\n")

lines = lines.split("\n")

tokens = set(tokens.split(", "))

global cache
cache = {}

def rec(line):
    global cache
    
    if line in cache: return cache[line]

    if line == "":
        return 1
    
    r = 0
    for t in tokens:
        if line.startswith(t):
            r += rec(line[len(t):])
            
    cache[line] = r
    return r


x = 0
i = 0
for line in lines:
    print(i)
    x += int(rec(line))
    i += 1

print(x)