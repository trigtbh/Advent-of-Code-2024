import aoc
contents = aoc.get_input(2024, 13).strip()
del aoc
# ---

machines = contents.split("\n\n")

total = 0

precision = 10

for machine in machines:
    b1, b2, target = machine.split("\n")

    target = list(map(int, [t.split("=")[1] for t in target.split(": ")[1].split(", ")]))
    target = [t+10000000000000 for t in target]
    
    aup = list(map(int, [t.split("+")[1] for t in b1.split(": ")[1].split(", ")]))
    bup = list(map(int, [t.split("+")[1] for t in b2.split(": ")[1].split(", ")]))
    

    # ideal solution ???

    a = float(aup[0])
    b = float(bup[0])
    c = float(aup[1])
    d = float(bup[1])

    c1, c2 = target


    # y = (c2 - (c * c1)/a)/(d - (c*b/a))
    # x = (c1 - b*y)/a


    y = (a*c2 - c*c1)/(a*d - c*b)
    x = (c1 - b*y)/a 

    
    if (abs(y - round(y)) < 10**-precision and abs(x - round(x)) < 10**-precision):
        # print(c*x, d*y, c*x+d*y, c2)
        # assert abs(a*x + b*y - c1) < 10**-precision
        # assert abs(c*x + d*y - c2) < 10**-precision
        total += (3 * x + y)

    # print(y, x)
    # input()


print(total)