import aoc
contents = aoc.get_input(2024, 22).strip()
del aoc
# ---

numbers = list(map(int, contents.split("\n")))

finals = []

def run(n):
    global x
    for i in range(2000):
        a = ((n * 64) ^ n) % 16777216
        b = (int(a / 32) ^ a) % 16777216
        n = ((b * 2048) ^ b) % 16777216
    finals.append(n)

import multiprocessing as mp

if __name__ == "__main__":
    for n in numbers:
        p = mp.Process(target=run, args=(n,))
        p.start()
        # p.join()


    while len(finals) != 1714:
        if len(finals) % 10 == 0:
            print(len(finals))