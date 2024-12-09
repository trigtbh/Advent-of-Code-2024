import aoc
contents = aoc.get_input(2024, 9).strip()
del aoc
# ---

freespaces = []
files = []

i = 0

pointer = 0

free = False
for char in contents:
    if not free:
        for n in range(int(char)):
            files.append(
                (i, pointer)
            )
            pointer += 1

        i += 1
    else:
        for n in range(int(char)):
            freespaces.append(
                pointer
            )
            pointer += 1


    free = not free

readjusted = []


# while True:
#     if readjusted and (readjusted[-1][1] == freespaces[0] - 1 or files[-1][1] == freespaces[0] - 1):
#         break


while freespaces[0] < files[-1][1]:
    pos = freespaces.pop(0)

    block = list(files.pop(-1))

    block[1] = pos
    # print(block)
    readjusted.append(block)


new = sorted(files + readjusted, key=lambda x: x[1])

checksum = 0
checksum = sum(
    i * item[0]
    for i, item in enumerate(new)


)

print(checksum)