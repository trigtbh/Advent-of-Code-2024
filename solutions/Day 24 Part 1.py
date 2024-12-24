import aoc
contents = aoc.get_input(2024, 24).strip()
del aoc
# ---

w, c = contents.split("\n\n")

wires = {}
for line in w.split("\n"):
    wire, val = line.split(": ")
    wires[wire] = int(val)

pairs = {

}

for line in c.split("\n"):
    param, target = line.split(" -> ")

    param = "(" + param.lower() + ")"
    param = param.replace("and", "&").replace("xor", "^").replace("or", "|")

    pairs[target] = param

while len(pairs) > 0:
    # print(len(pairs))
    k = set(pairs.keys())
    for item in k:
        count = 0
        exp = pairs[item]
        for wire in wires:
            if wire in exp: count += 1
            exp = exp.replace(wire, str(wires[wire]))
        # print(count)
        if count == 2:
            wires[item] = eval(exp)
            del pairs[item]
    # input()

s = ""
for pair in sorted(wires.items()):
    if pair[0][0] == "z":
        s += str(pair[1])

print(int(s[::-1], 2))

# print(sorted(wires.items()))