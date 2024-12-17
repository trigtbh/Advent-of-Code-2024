import aoc
contents = aoc.get_input(2024, 17).strip()
del aoc
# ---

registers = {}

rtext, ptext = contents.split("\n\n")

for i in range(3):
    num = int(rtext.split("\n")[i].split(": ")[1])
    registers[
        "ABC"[i]
    ] = num

pairs = []
ptext = ptext.split(": ")[1].split(",")
for i in range(len(ptext) // 2):
    pairs.append(
        (int(ptext[2*i]), int(ptext[2*i+1]))
    )

output = []

inst = 0
while 0 <= inst < len(pairs):
    opcode, operand = pairs[inst]
    movenext = True

    combo = 0
    if 0 <= operand <= 3:
        combo = operand
    elif operand == 4:
        combo = registers["A"]
    elif operand == 5:
        combo = registers["B"]
    elif operand == 6:
        combo = registers["C"]
    elif operand == 7:
        raise ValueError("operand 7")

    # print(opcode, operand, combo)

    if opcode == 0:
        # adv
        n = registers["A"]
        d = 2 ** combo
        registers["A"] = int(n / d)
    if opcode == 1:
        n = registers["B"]
        registers["B"] = n ^ operand
    if opcode == 2:
        registers["B"] = combo % 8
    if opcode == 3:
        if registers["A"] != 0:
            movenext = False
            inst = int(operand / 2)
    if opcode == 4:
        registers["B"] = registers["B"] ^ registers["C"]
    if opcode == 5:
        output.append(combo % 8)
    if opcode == 6:
        n = registers["A"]
        d = 2 ** combo
        registers["B"] = int(n / d)
    if opcode == 7:
        n = registers["A"]
        d = 2 ** combo
        registers["C"] = int(n / d)
    
    if movenext:
        inst = inst + 1

print(",".join(list(map(str, output))))