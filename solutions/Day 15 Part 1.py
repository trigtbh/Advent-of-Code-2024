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
    

grid, directions = contents.split("\n\n")
grid = grid.split("\n")

walls = set()
boxes = dict()

directions = directions.replace("\n", "")

robot = None

for y in range(len(grid)):
    for x in range(len(grid[0])):
        if grid[y][x] == "#":
            walls.add((y, x))
        if grid[y][x] == "@":
            robot = Box(x, y, boxes, walls)
            robot.not_robot = False
        if grid[y][x] == "O":
            boxes[(y, x)] = Box(x, y, boxes, walls)
        
test = boxes[list(boxes.keys())[0]] 
for t in boxes:
    b = boxes[t]
    assert b.walls == test.walls 
    assert b.boxes == test.boxes

mapped = {
    "^": 1,
    ">": 2,
    "v": 3,
    "<": 4
}

i = 0
for d in directions:
    robot.push(mapped[d])
    i += 1

m = 0
for t in boxes:
    b = boxes[t]
    m += (100 * b.y + b.x)

print(m)