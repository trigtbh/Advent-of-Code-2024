import aoc
contents = aoc.get_input(2024, 11).strip()
del aoc
# ---

nums = list(map(int, contents.split(" ")))

nums = {
    n: 1 for n in nums
}


for i in range(75):
    # print(sum(v for v in nums.values()))
    
    n = {}
    for num in nums:
        line = []
        if num == 0:
            line.append(1)
        elif len(str(num)) % 2 == 0:
            s = str(num)
            # print(s)
            l = int(len(s) / 2)
            line.append(int(s[:l]))
            line.append(int(s[l:]))
        else:
            line.append(num * 2024)

        for number in line:
            if number not in n:
                n[number] = 0
            # n[number] += 1
            # if number in nums:
            #     n[number] += nums[number]
            # else:
            #     n[number] += 1
            n[number] += nums[num]

    # n = {
    #     k: v * (1 if v not in nums else nums[v])
    #     for k, v in n.items()
    # }


    nums = n
    # print(nums)
    # input()

# print(nums)
print(sum(v for k, v in nums.items()))