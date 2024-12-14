import aoc
contents = aoc.get_input(2024, 14).strip()
del aoc
# ---

class Robot:
    def __init__(self, x, y, vx, vy, maxx, maxy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.maxx = maxx
        self.maxy = maxy

        self.midx = int(maxx / 2)
        self.midy = int(maxy / 2)

    def tick(self):
        self.x += self.vx
        self.y += self.vy

        while self.x < 0:
            self.x += self.maxx
        while self.y < 0:
            self.y += self.maxy

        self.x %= self.maxx
        self.y %= self.maxy
        
    def cat(self):
        if self.x == self.midx or self.y == self.midy: return 5
        if self.x < self.midx:
            if self.y < self.midy:
                return 1
            return 3
        else:
            if self.y < self.midy:
                return 2
            return 4

        

robots = contents.split("\n")
mx = 0
my = 0
for r in robots:
    p, v = r.split(" ")
    p = p.split("=")[1]
    px, py = list(map(int, p.split(",")))
    mx = max(mx, px + 1)
    my = max(my, py + 1)



# mx, my = 11, 7

robots_real = []
for r in robots:
    p, v = r.split(" ")
    p = p.split("=")[1]
    v = v.split("=")[1]
    px, py = list(map(int, p.split(",")))
    vx, vy = list(map(int, v.split(",")))
    robots_real.append(
        Robot(px, py, vx, vy, mx, my)
    )


cats = [[], [], [], [], []]

for r in robots_real:
    for _ in range(100):
        r.tick()
        # print(r.x, r.y)
        # input()

    cats[r.cat() - 1].append(r)




print(len(cats[0]) * len(cats[1]) * len(cats[2]) * len(cats[3]))