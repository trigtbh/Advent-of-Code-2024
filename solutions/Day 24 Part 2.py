import aoc
contents = aoc.get_input(2024, 24).strip()
del aoc
# ---

w, c = contents.split("\n\n")

wires = {}
for line in w.split("\n"):
    wire, val = line.split(": ")
    # wires[wire] = val
    wires[wire] = wire

pairs = {

}

for line in c.split("\n"):
    param, target = line.split(" -> ")

    # param = "(" + param.lower() + ")"
    param = param.lower()
    param = param.replace("and", "&").replace("xor", "^").replace("or", "|")

    pairs[target] = param


adder = set()

for out, exp in pairs.items():
    left, op, right = exp.split(" ")
    
    left, right = sorted([left, right])

    adder.add(
        (left, op, right, out)
    )

malformed = set()

def is_part_of_or(tag):
    ...
    return any(
        op == "|"
        and (tag == a or tag == b)
        for a, op, b, _ in adder
    )

for (left, op, right, out) in adder:
    if out[0] == "z" and op != "^" and out != "z45": # output must always be the result of an XOR op
        # unless it's the first bit in the result
        # then it's supposed to be the result of an OR (the last carry bit)
        malformed.add(out)
    elif op == "^" and not(left[0] == "x" or right[0] == "y" or out[0] == "z"):
        # XORs should only take in x/y vals, or only output z
        malformed.add(out)
    elif op == "&" and left != "x00" and not is_part_of_or(out):
        # AND outputs should only lead to ORs
        malformed.add(out)

    elif op == "^" and is_part_of_or(out):
        # XOR should not lead to ORs (can lead to XORs or ANDs, or nothing)
        malformed.add(out)

    

print(",".join(sorted(malformed)))