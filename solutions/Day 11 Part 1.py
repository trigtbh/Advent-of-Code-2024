import aoc
contents = aoc.get_input(2024, 11).strip()
del aoc
# ---

nums = list(map(int, contents.split(" ")))


for i in range(25):
    print(i)
    n = []
    for num in nums:
        if num == 0:
            n.append(1)
        elif len(str(num)) % 2 == 0:
            s = str(num)
            # print(s)
            l = int(len(s) / 2)
            n.append(int(s[:l]))
            n.append(int(s[l:]))



        else:
            n.append(num * 2024)

    nums = n

print(len(nums))