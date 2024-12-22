import aoc
contents = aoc.get_input(2024, 22).strip()
del aoc
# ---

numbers = list(map(int, contents.split("\n")))

x = 0

for n in numbers:
    for i in range(2000):
        a = ((n * 64) ^ n) % 16777216
        b = (int(a / 32) ^ a) % 16777216
        n = ((b * 2048) ^ b) % 16777216
    x += n

print(x)