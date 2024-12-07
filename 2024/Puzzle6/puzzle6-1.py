direction = "N"
sum = 0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def move(pos: Point):
    global direction
    global sum
    global grid

    nexPos: Point
    nexDir: str
    if direction == "N":
        nexPos = Point(pos.x, pos.y-1)
        nexDir = "E"
    elif direction == "E":
        nexPos = Point(pos.x+1, pos.y)
        nexDir = "S"
    elif direction == "S":
        nexPos = Point(pos.x, pos.y+1)
        nexDir = "W"
    elif direction == "W":
        nexPos = Point(pos.x-1, pos.y)
        nexDir = "N"
    
    if not 0 <= nexPos.x < len(grid[0]) or not 0 <= nexPos.y < len(grid):
        sum += 1
        return nexPos

    if grid[nexPos.y][nexPos.x] == "#":
        direction = nexDir
        return pos
        
    if grid[nexPos.y][nexPos.x] != "X":
        sum += 1
        
    temp = list(grid[pos.y])
    temp[pos.x] = "X"
    grid[pos.y] = "".join(temp)
    
    return nexPos


def find_start() -> Point:
    global grid
    for i, row in enumerate(grid):
        for char in row:
            if char == "^":
                return Point(row.index(char), i)

def traverse_file(fileName: str) -> [[int]]:
    file = open(fileName)
    lines = file.read().split()

    return lines


grid = traverse_file("input.txt")
position = find_start()

while 0 <= position.x < len(grid[0]) and 0 <= position.y < len(grid):
    position = move(position)
print(grid)

print(sum)