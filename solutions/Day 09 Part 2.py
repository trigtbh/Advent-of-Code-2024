import aoc
contents = aoc.get_input(2024, 9).strip()
del aoc
# ---


class File:
    def __init__(self, id_, length):
        self.id = id_
        self.length = length
        self.fixed = False

    def __repr__(self):
        return ("FIXED_" if self.fixed else "") + f"File(id={self.id}, length={self.length})"





class FreeSpace:
    def __init__(self, length):
        self.length = length

    
    def __repr__(self):
        return f"Space(length={self.length})"






fs = []

i = 0

pointer = 0


blocks = 0

free = False
for char in contents:
    if not free:
        fs.append(File(i, int(char)))
        i += 1
    else:
        fs.append(FreeSpace(int(char)))
        blocks += 1
    free = not free

# readjusted = []

i = len(fs) - 1
while i >= 0:

    # for item in fs:
    #     if isinstance(item, File):
    #         print(str(item.id) * item.length, end="")
    #     else:
    #         print("." * item.length, end="")
    # input()



    item = fs.pop(i)

    if isinstance(item, FreeSpace):
        
        fs.insert(i,item)
        i -= 1
        continue
        
    else:
        if item.fixed:
            i -= 1
            continue
    
        found = False
        for j in range(0, i):
            
            item2 = fs[j]
            if isinstance(item2, FreeSpace):
                if item2.length >= item.length:
                    new = FreeSpace(item2.length - item.length)

                    fs.insert(j,item)
                    fs[j+1] = new
                    
                    fs.insert(i+1, FreeSpace(item.length))
                    if new.length == 0:
                        del fs[j + 1]
                        i -= 1
                    found = True
                    break


        if not found:
            item.fixed = True
            fs.insert(i,item)
            i -= 1

    # print(fs)

    
# print(fs)

new = []
i = 0
for item in fs:
    if isinstance(item, File):
        for n in range(item.length):
            new.append((item.id, i))
            i += 1
    else:
        i += item.length

print(sum(x[0] * x[1] for x in new))
# # while True:
# #     if readjusted and (readjusted[-1][1] == freespaces[0] - 1 or files[-1][1] == freespaces[0] - 1):
# #         break


# while freespaces[0] < files[-1][1]:
#     pos = freespaces.pop(0)

#     block = list(files.pop(-1))

#     block[1] = pos
#     # print(block)
#     readjusted.append(block)


# new = sorted(files + readjusted, key=lambda x: x[1])

# checksum = 0
# checksum = sum(
#     i * item[0]
#     for i, item in enumerate(new)


# )

# print(checksum)