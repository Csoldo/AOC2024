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
