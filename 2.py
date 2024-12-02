import time
from copy import deepcopy

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/2.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")

    matrix = [[int(x) for x in line.split()] for line in lines]
    return matrix

def first_part():
    data = read_input()
    cnt = 0
    for row in data:
        ascending = row[0] < row[1]
        safe = True
        for i in range(0, len(row)-1):
            if ascending:
                diff = row[i+1] - row[i]
                if diff > 3 or diff < 1:
                    safe = False
                    break
            else:
                diff = row[i] - row[i+1]
                if diff > 3 or diff < 1:
                    safe = False
                    break
        if safe:
            cnt += 1
    return cnt

start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")

def second_part():
    data = read_input()
    cnt = 0
    def check_row(row: list):
        ascending = row[0] < row[1]
        for i in range(0, len(row)-1):
            if ascending:
                diff = row[i+1] - row[i]
                if diff > 3 or diff < 1:
                    return False
            else:
                diff = row[i] - row[i+1]
                if diff > 3 or diff < 1:
                    return False
        return True
    
    for row in data:
        safe = check_row(row)
        
        if safe:
            cnt += 1
        else:
            for i in range(len(row)):
                copied = deepcopy(row)
                copied.pop(i)
                safe = check_row(copied)
                if safe:
                    cnt += 1
                    break
    return cnt

start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")
