import aoc
contents = aoc.get_input(2024, 7).strip()
del aoc
# ---

def rec(n, nums, target):
    if n > target: return False
    if len(nums) == 0:
        return n == target
    
    return rec(n * nums[0], nums[1:], target) or rec(n + nums[0], nums[1:], target) or rec(int(str(n) + str(nums[0])), nums[1:], target)


x = 0
for line in contents.split("\n"):
    target, nums = line.split(": ")
    target = int(target); nums = list(map(int, nums.split(" ")))

    if rec(nums[0], nums[1:], target):

        x += target

print(x)