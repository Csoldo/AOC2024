import time

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/6.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")
    return lines


def first_part():
    data = read_input()
    row_size = len(data[0])
    col_size = len(data)
    guard = None
    for i in range(row_size):
        for j in range(col_size):
            curr = data[i][j]
            if curr in "v><^":
                if curr == 'v':
                    guard_dir = "down"
                elif curr == '>':
                    guard_dir = "right"
                elif curr == '<':
                    guard_dir = "left"
                else:
                    guard_dir = "up"
                guard = (i, j)
                break

    sum = 0
    while True:
        i = guard[0]
        j = guard[1]
        if data[i][j] != "x":
            line = data[i]
            data[i] = line[:j] + 'x' + line[j+1:]
            sum += 1
        if guard_dir == "up":
            i -= 1
        elif guard_dir == "right": 
            j += 1
        elif guard_dir == "down":
            i += 1
        elif guard_dir == "left":
            j -= 1


        if i < 0 or j < 0 or i > row_size - 1 or j > col_size - 1:
            break

        next = data[i][j]
        curr = data[guard[0]][guard[1]]
        if next == "#":
            if guard_dir == "up":
                i += 1
                j += 1
                guard_dir = "right"
            elif guard_dir == "right":
                j -= 1
                i += 1
                guard_dir = "down"
            elif guard_dir == "down":
                j -= 1
                i -= 1
                guard_dir = "left"
            elif guard_dir == "left":
                j += 1
                i -= 1
                guard_dir = "up"
            if i < 0 or j < 0 or i > row_size - 1 or j > col_size - 1:
                break
        
        guard = (i, j)
    return sum

start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")



def second_part():
    data = read_input()
    row_size = len(data[0])
    col_size = len(data)

    def print_data():
        for line in data:
            print(line)
        print("\n")
    guard = None
    guard_route = []
    for i in range(row_size):
        for j in range(col_size):
            curr = data[i][j]
            if curr in "v><^":
                if curr == 'v':
                    guard_dir = "down"
                elif curr == '>':
                    guard_dir = "right"
                elif curr == '<':
                    guard_dir = "left"
                else:
                    guard_dir = "up"
                guard = (i, j)
                break
    sum = 0
    print(guard)
    print(guard_dir)
    while True:
        i = guard[0]
        j = guard[1]
        guard_route.append((i,j, guard_dir))
        print_data()
        prev_i = guard[0]
        prev_j = guard[1]
        if data[i][j] not in "+":
            line = data[i]
            added_char = "|" if guard_dir in ["up", "down"] else '-'
            if (data[i][j] == "|" and added_char == "-") or (data[i][j] == "-" and added_char == "|"):
                added_char = "+"
            data[i] = line[:j] + added_char + line[j+1:]
            sum += 1

        if guard_dir == "up":
            i -= 1
        elif guard_dir == "right": 
            j += 1
        elif guard_dir == "down":
            i += 1
        elif guard_dir == "left":
            j -= 1


        if i < 0 or j < 0 or i > row_size - 1 or j > col_size - 1:
            break

        next = data[i][j]

        curr = data[prev_i][prev_j]
        if next == "#":
            if guard_dir == "up":
                i += 1
                j += 1
                guard_dir = "right"
            elif guard_dir == "right":
                j -= 1
                i += 1
                guard_dir = "down"
            elif guard_dir == "down":
                j -= 1
                i -= 1
                guard_dir = "left"
            elif guard_dir == "left":
                j += 1
                i -= 1
                guard_dir = "up"
            data[prev_i] = line[:prev_j] + "+" + line[prev_j+1:]
            if i < 0 or j < 0 or i > row_size - 1 or j > col_size - 1:
                break
        
        guard = (i, j)
    print_data()
    for step, (i,j, dir) in enumerate(guard_route):
        print(f"step: {step}, i: {i}, j: {j}, dir: {dir}")
        if step >= len(guard_route) - 1:
            break
        
        # (obstacle_loc_i, obstacle_loc_j) = (i, j)
        # (next_i, next_j, next_dir) = guard_route[step+1]



start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")

