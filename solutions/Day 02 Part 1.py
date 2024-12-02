import aoc
contents = aoc.get_input(2024, 2).strip()
del aoc

# ---

safe = 0
lines = contents.split("\n")
for line in lines:
    nums = list(map(int, line.split(" ")))
    d = 0
    for i in range(len(nums) - 1):
        if d == 0:
            if nums[i] < nums[i + 1]:
                d = 1
            elif nums[i] > nums[i + 1]:
                d = -1
            else:
                break
        if nums[i] == nums[i + 1]:
            break
        if nums[i] < nums[i + 1] and d != 1:
            break
        if nums[i] > nums[i + 1] and d != -1:
            break
        if not(1 <= abs(nums[i] - nums[i + 1]) <= 3):
            break
    else:
        safe += 1
print(safe)