from copy import deepcopy
import time

class Point:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x},{self.y})"

def flatten(xss):
    return [x for xs in xss for x in xs]

def read_input():
    input_file = "inputs/example.in"
    # input_file = "inputs/15.in"
    with open(input_file) as f:
        lines = f.read()
    
    lines = lines.split("\n")
    read_map = True
    
    map = []
    movements = []
    for i, line in enumerate(lines):
        if line == '':
            read_map = False
            continue

        if read_map:
            if "@" in line:
                location = Point(i, line.index("@"))
            map.append([x if x != '@' else '.' for x in line])

        else:
            movements.append([x for x in line])

    movements = flatten(movements)

    return map, movements, location

def print_map(map, robot):
    map_copy = deepcopy(map)
    map_copy[robot.x][robot.y] = "@"

    for x in map_copy:
        print("".join(x))
    print("\n")

def next_location(move, p: Point):
    robot = deepcopy(p)
    if move == "<":
        robot.y -= 1
    elif move == ">":
        robot.y += 1
    elif move == "v":
        robot.x += 1
    else:
        robot.x -= 1
    return robot

def column(matrix, i):
    return [row[i] for row in matrix]

def last_index(row):
    for i in range(len(row)-1, -1, -1):
        if row[i] == ".":
            return i
        elif row[i] == "#":
            raise ValueError
        
def index(row):
    for i in range(len(row)):
        if row[i] == ".":
            return i
        elif row[i] == "#":
            raise ValueError
    

def first_part():
    map, movements, robot = read_input()
    col_size = len(map[0])
    for move in movements:
        target = next_location(move, robot)
        next = map[target.x][target.y]
        if next == ".":
            robot = target
        elif next == "#":
            continue
        elif next == "O":
            if move == ">":
                try:
                    free_space = index(map[target.x][target.y:col_size])
                    map[target.x][target.y] = "."
                    map[target.x][free_space+target.y] = "O"
                    robot = target
                except ValueError:
                    continue
            elif move == "<":
                try:
                    free_space = last_index(map[target.x][0:target.y])
                    map[target.x][target.y] = "."
                    map[target.x][free_space] = "O"
                    robot = target
                except ValueError:
                    continue
            elif move == "v":
                try:
                    col = column(map, target.y)
                    free_space = index(col[target.x:col_size])
                    map[target.x][target.y] = "."
                    map[free_space+target.x][target.y] = "O"
                    robot = target
                except ValueError:
                    continue
            elif move == "^":
                try:
                    col = column(map, target.y)
                    free_space = last_index(col[0:target.x])
                    map[target.x][target.y] = "."
                    map[free_space][target.y] = "O"
                    robot = target
                except ValueError:
                    continue
        

    result = 0
    for i, row in enumerate(map):
        for j, x in enumerate(row):
            if map[i][j] == "O":
                result += 100*i + j
    print_map(map, robot)
    return result

start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")

