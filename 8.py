import time

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/8.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")
    return lines

def first_part():
    data = read_input()
    keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    map = dict(zip(keys, [[] for _ in keys]))

    rowsize = len(data[0])
    colsize = len(data)

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != ".":
                map[char].append((i,j))

    antinodes = []
    for key in map:
        values = map[key]
        values.sort()
        if len(values) > 1:
            for i in range(len(values)-1):
                for j in range(i+1, len(values)):
                    x, y = values[i]
                    x_hat, y_hat = values[j]
                    i_new = x + (x - x_hat)
                    j_new = y + (y - y_hat)
                    if 0 <= i_new < rowsize and 0 <= j_new < colsize:
                        new = (i_new, j_new)
                        if new not in antinodes:
                            antinodes.append(new)
                    
                    i_new = x_hat - (x - x_hat)
                    j_new = y_hat - (y - y_hat)
                    if 0 <= i_new < rowsize and 0 <= j_new < colsize:
                        new = (i_new, j_new)
                        if new not in antinodes:
                            antinodes.append(new)

    return len(antinodes)

start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")


def second_part():
    data = read_input()
    keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    map = dict(zip(keys, [[] for _ in keys]))

    rowsize = len(data[0])
    colsize = len(data)

    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if char != ".":
                map[char].append((i,j))

    antinodes = []
    for key in map:
        values = map[key]
        values.sort()
        if len(values) > 1:
            for i in range(len(values)-1):
                for j in range(i+1, len(values)):
                    x, y = values[i]
                    x_hat, y_hat = values[j]

                    if values[i] not in antinodes:
                        antinodes.append(values[i])
                    if values[j] not in antinodes:
                        antinodes.append(values[j])
                    i_new = x
                    j_new = y
                    while True:
                        i_new += (x - x_hat)
                        j_new += (y - y_hat)
                        if 0 <= i_new < rowsize and 0 <= j_new < colsize:
                            new = (i_new, j_new)
                            if new not in antinodes:
                                antinodes.append(new)
                        else:
                            break
                    
                    i_new = x_hat
                    j_new = y_hat
                    while True:
                        i_new -= (x - x_hat)
                        j_new -= (y - y_hat)
                        if 0 <= i_new < rowsize and 0 <= j_new < colsize:
                            new = (i_new, j_new)
                            if new not in antinodes:
                                antinodes.append(new)
                        else:
                            break
    return len(antinodes)

start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")
