import time

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/10.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")
    data = []
    for line in lines:
        data.append([(int(x) if x != '.' else -1) for x in line])
    
    return data



def find_path(x, y, sum, data, found_end_points):
    row_size = len(data)
    col_size = len(data[0])
    if data[x][y] == 9:
        if found_end_points[x][y]:
            return sum
        else:
            found_end_points[x][y] = True
            return (sum + 1)
            
    if x < row_size - 1 and (data[x][y] - data[x+1][y]) == -1:
        sum = find_path(x+1, y, sum, data, found_end_points)
    
    if x > 0 and data[x][y] - data[x-1][y] == -1:
        sum = find_path(x-1, y, sum, data, found_end_points)
    
    if y > 0 and data[x][y] - data[x][y-1] == -1:
        sum = find_path(x, y-1, sum, data, found_end_points)
    
    if y < col_size - 1 and data[x][y] - data[x][y+1] == -1:
        sum = find_path(x, y+1, sum, data, found_end_points)

    return sum


def first_part():
    data = read_input()
    final_sum = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                found_end_points = [[False for x in line] for line in data]
                final_sum = find_path(i, j, 0, data, found_end_points)

    return final_sum

start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")

def find_distinct_path(x, y, sum, data):
    row_size = len(data)
    col_size = len(data[0])
    if data[x][y] == 9:
        return (sum + 1)
            
    if x < row_size - 1 and (data[x][y] - data[x+1][y]) == -1:
        sum = find_distinct_path(x+1, y, sum, data)
    
    if x > 0 and data[x][y] - data[x-1][y] == -1:
        sum = find_distinct_path(x-1, y, sum, data)
    
    if y > 0 and data[x][y] - data[x][y-1] == -1:
        sum = find_distinct_path(x, y-1, sum, data)
    
    if y < col_size - 1 and data[x][y] - data[x][y+1] == -1:
        sum = find_distinct_path(x, y+1, sum, data)
    
    return sum


def second_part():
    data = read_input()
    final_sum = 0

    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 0:
                final_sum = find_distinct_path(i, j, 0, data)

    return final_sum

start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")

