import aoc
contents = aoc.get_input(2024, 2).strip()
del aoc

# ---

def test(nums):
    d = 0
    for i in range(len(nums) - 1):
        if d == 0:
            if nums[i] < nums[i + 1]:
                d = 1
            elif nums[i] > nums[i + 1]:
                d = -1
            else:
                return False, i
        if nums[i] == nums[i + 1]:
            return False, i
        if nums[i] < nums[i + 1] and d != 1:
            return False, i
        if nums[i] > nums[i + 1] and d != -1:
            return False, i
        if not(1 <= abs(nums[i] - nums[i + 1]) <= 3):
            return False, i
    else:
        return True, i


safe = 0
lines = contents.split("\n")
for line in lines:
    nums = list(map(int, line.split(" ")))
    res, val  = test(nums)
    go = True
    
    if not res:
        go = False
        for i in range(len(nums)):
            if test(nums[:i] + nums[i+1:])[0]:
                go = True
                break


    if go: 
        # print("safe ->", nums)
        safe += 1
    else:
        continue
        print("unsafe")

print(safe)