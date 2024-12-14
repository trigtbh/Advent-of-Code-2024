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

i = 0

print("\n" * 200)

attempt = 0
while True:
    
    full = {}
    for r in robots_real:
        for _ in range(1):
            r.tick()
        full[(r.x, r.y)] = r
    

    display = False
    for point in full.keys():
        px, py = point
        if all(
            [(px + diag+1, py + diag+1) in full for diag in range(10)]
            
        ):
            display = True
            break
        
        
    if display:
        n = sorted(full.values(), key = lambda r: (r.y, r.x))
        p = 0
        # print(n)
        for y in range(my):
            for x in range(mx):
                if p < len(n) and n[p].x == x and n[p].y == y:
                    print("#", end="")
                    p += 1
                else:
                    print(" ", end="")
            print("")
    i += 1

    if display:
        try:
            input("Ctrl+C to exit and see the final number.")
        except:
            print(i)
            break
        print("\n" * 200)