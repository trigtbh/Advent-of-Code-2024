import aoc
contents = aoc.get_input(2024, 15).strip()
del aoc
# ---

class Box:
    def __init__(self, x, y, boxes, walls):
        self.x = x
        self.y = y
        self.boxes = boxes
        self.walls = walls
        self.not_robot = True
        self.linked = None

    def gps(self):
        # if self.linked.x < self.x:
        #     return self.linked.gps()
    
        return 100*self.y + self.x

    def __repr__(self):
        return f"Box({self.y}, {self.x})"
    
    def nudge(self, direction):
        nx = self.x
        ny = self.y

        if direction == 1:
            ny -= 1
        if direction == 2:
            nx += 1
        if direction == 3:
            ny += 1
        if direction == 4:
            nx -= 1

        return (ny, nx)

    def scan(self, direction, points, dontinclude=False):
        nx = self.x
        ny = self.y

        if direction == 1:
            ny -= 1
        if direction == 2:
            nx += 1
        if direction == 3:
            ny += 1
        if direction == 4:
            nx -= 1


        valid = True
        if (ny, nx) in self.walls:
            valid = False

        if (ny, nx) in self.boxes:
            valid = self.boxes[(ny, nx)].scan(direction, points)

        if not dontinclude and valid:
            valid = valid and self.linked.scan(direction, points, dontinclude=True)
            

        if not valid:
            while len(points) > 0:
                points.pop()
        else:
            points.add(self)
        

        return valid

        
    def push(self, direction):
        nx = self.x
        ny = self.y

        if direction == 1:
            ny -= 1
        if direction == 2:
            nx += 1
        if direction == 3:
            ny += 1
        if direction == 4:
            nx -= 1

        valid = True
        if (ny, nx) in self.walls:
            valid = False
        elif (ny, nx) in self.boxes:
            valid = self.boxes[(ny, nx)].push(direction)
        
        if valid:

            # 
            if self.not_robot:
                self.boxes[(ny, nx)] = self
            else:
                if (ny, nx) in boxes:
                    del self.boxes[(ny, nx)]


            self.x = nx
            self.y = ny
        return valid


class Robot:
    def __init__(self, x, y, boxes, walls):
        self.x = x
        self.y = y
        self.boxes = boxes
        self.walls = walls
        self.not_robot = True

    def push(self, direction):
        nx = self.x
        ny = self.y

        willscan = False
        if direction == 1:
            ny -= 1
            willscan = True
        if direction == 2:
            nx += 1
        if direction == 3:
            ny += 1
            willscan = True
        if direction == 4:
            nx -= 1

        # print(ny, nx)
        if not willscan:
            valid = True
            if (ny, nx) in self.walls:
                valid = False
            elif (ny, nx) in self.boxes:
                valid = self.boxes[(ny, nx)].push(direction)
            
            if valid:

                # 
                if self.not_robot:
                    self.boxes[(ny, nx)] = self
                else:
                    if (ny, nx) in boxes:
                        del self.boxes[(ny, nx)]


                self.x = nx
                self.y = ny
            return valid

        else:
            valid = True
            scanned = set()
            if (ny, nx) in self.walls:
                valid = False
            elif (ny, nx) in self.boxes:
                valid = self.boxes[(ny, nx)].scan(direction, scanned)
                

            if valid:
                for b in scanned:
                    del self.boxes[(b.y, b.x)]
                    
                for b in scanned:
                    bny, bnx = b.nudge(direction)
                    self.boxes[(bny, bnx)] = b
                    b.y = bny
                    b.x = bnx
                
                # 
                # if self.not_robot:
                #     self.boxes[(ny, nx)] = self
                # else:
                #     if (ny, nx) in boxes:
                #         del self.boxes[(ny, nx)]


                self.x = nx
                self.y = ny
            return valid



grid, directions = contents.split("\n\n")
grid = grid.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")
grid = grid.split("\n")

walls = set()
boxes = dict()
leftside = set()

directions = directions.replace("\n", "")

robot = None

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            walls.add((y, x))
        if grid[y][x] == "@":
            robot = Robot(x, y, boxes, walls)
            robot.not_robot = False
        if grid[y][x] == "[":
            boxes[(y, x)] = Box(x, y, boxes, walls)
            leftside.add(boxes[(y, x)])
        if grid[y][x] == "]":
            boxes[(y, x)] = Box(x, y, boxes, walls)    
            boxes[(y, x-1)].linked = boxes[(y, x)]
            boxes[(y, x)].linked = boxes[(y, x-1)]
        
test = boxes[list(boxes.keys())[0]] 
for t in boxes:
    b = boxes[t]
    assert b.walls == test.walls 
    assert b.boxes == test.boxes

reallength = len(boxes)

mapped = {
    "^": 1,
    ">": 2,
    "v": 3,
    "<": 4
}

i = 0
for d in directions:
    # print(d)
    robot.push(mapped[d])
    
    # for y in range(len(grid)):
    #     for x in range(len(grid[0])):
    #         if (y, x) in walls:
    #             print("#", end="")
    #         elif (y, x) in boxes:
    #             if boxes[(y, x)] in leftside:
    #                 print("[", end="")
    #             else:
    #                 print("]", end="")
    #         elif y == robot.y and x == robot.x:
    #             print("@", end="")
    #         else:
    #             print(".", end="")
    #     print()

    # input()
    # print("\n" * 100)



    assert len(boxes) == reallength
    i += 1

m = 0
realleft = sorted([
    (b.y, b.x) for b in leftside
])
# print(realleft)
for b in realleft:
    # b = boxes[t]

    m += boxes[b].gps()

print(m)