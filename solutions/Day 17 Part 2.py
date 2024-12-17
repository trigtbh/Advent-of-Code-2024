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

registers["A"] = "A"

pairs = []
ptext = ptext.split(": ")[1].split(",")
for i in range(len(ptext) // 2):
    pairs.append(
        (int(ptext[2*i]), int(ptext[2*i+1]))
    )

output = []

inst = 0

while len(output) != len(pairs) * 2:
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
        registers["A"] = f"({n} // (2 ** {combo}))"
    if opcode == 1:
        n = registers["B"]
        registers["B"] = f"({n} ^ {operand})"
    if opcode == 2:
        registers["B"] = f"({combo} % 8)"
    if opcode == 3:
        inst = 0
        movenext = False
        # if registers["A"] != 0:
        #     movenext = False
        #     inst = int(operand / 2)
    if opcode == 4:
        # registers["B"] = registers["B"] ^ registers["C"]
        registers["B"] = f"(({registers['B']}) ^ ({registers['C']}))"
    if opcode == 5:
        output.append(
            f"({combo} % 8)"
        )
    if opcode == 6:
        n = registers["A"]
        registers["B"] = f"int(({n}) / (2 ** {combo}))"
    if opcode == 7:
        n = registers["A"]
        registers["C"] = f"int(({n}) / (2 ** {combo}))"
    
    if movenext:
        inst = inst + 1

ptext = list(map(int, ptext))
ptextreal = ptext.copy()

A = 0

def sp(A):
    a = bin(A)[2:]
    while len(a) % 3 != 0:
        a = "0" + a
    return  ' '.join([a[i:i+3] for i in range(0, len(a), 3)])

final = []

def rec(A, ptext):
    # print(A)
    # print(bin(A), ptext)

    if len(ptext) == 0:
        A = A >> 3
        for i in  range(len(output)):
            l = output[::-1][i]
            expected = ptextreal[::-1][i]
            
            if eval(l) != expected:
                
                print(sp(A), eval(l), expected)
                break
        else:
            final.append(A)
        return

    for digit in ptext:
        for i in range(8):
            if ((i ^ 5) ^ 6 ^ ((A + i) // 2 ** (i ^ 5))) % 8 == digit:
                Ac = (A + i) * 8
                rec(Ac, ptext[1:])
        else:
            return
        

# ptext = [2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0]
rec(0, ptext[::-1])
print(min(final))