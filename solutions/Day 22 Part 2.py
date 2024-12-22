import aoc
contents = aoc.get_input(2024, 22).strip()
del aoc
# ---

numbers = list(map(int, contents.split("\n")))

final = {}

sequences = []

point = 0

for n in numbers:
    pairs = [(int(str(n)[-1]), 0)]

    seqprices = {}
    f = 0

    for i in range(2000):
        a = ((n * 64) ^ n) % 16777216
        b = (int(a / 32) ^ a) % 16777216
        n = ((b * 2048) ^ b) % 16777216

        pairs.append(
            (int(str(n)[-1]), int(str(n)[-1]) - pairs[-1][0])
        )

        f += 1
        if f >= 4:
            seq = tuple(p[1] for p in pairs[-4:])
            if seq not in seqprices: seqprices[seq] = int(str(n)[-1])

    # print(seqprices)
    sequences.append(seqprices)
    point += 1

keys = set()
for d in sequences:
    # print(d.keys())
    keys |= set(d.keys())

maxval = 0
for k in keys:
    v = 0
    for d in sequences:
        if k in d:
            v += d[k]
    if v > maxval:
        maxval = v

print(maxval)