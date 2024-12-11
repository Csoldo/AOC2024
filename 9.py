import time
from copy import deepcopy

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/9.in"
    with open(input_file) as f:
        lines = f.read()

    index = 0
    result = []
    files = [] #(start index, size, fileIndex) 
    for i, c in enumerate(lines):
        size = int(c)
        if i % 2 == 0:
            files.append((len(result),size, index))
            for _ in range(size):
                result.append(index)
            index += 1
        else:
            for _ in range(size):
                result.append(-1)
    return result, files


def print_data(data):
    for c in data:
        if c == -1:
            print(".", end="")
        else:
            print(c, end="")

def first_part():
    data, _ = read_input()
    last_dot_index = len(data) - 1
    first_dot_index = data.index(-1)
    while True:
        if last_dot_index <= first_dot_index+1:
            break
        # print_data(data)
        # print()
        for i in range(last_dot_index, first_dot_index, -1):
            if data[i] != -1:
                data[first_dot_index] = data[i]
                data[i] = -1 
                last_dot_index = i
                first_dot_index = data.index(-1)
                break
    sum = 0
    # print_data(data)
    for i, c in enumerate(data):
        if c == -1:
            break
        sum += i * int(c)

    return sum


# start_time = time.perf_counter()
# first = first_part()
# end_time = time.perf_counter()
# print("First part: ", first)
# execution_time = (end_time - start_time) * 1000
# print(f"Execution time: {execution_time:.4f} ms")

def second_part():
    data, files = read_input()
    #File: (start, size, file)
    file_indices = [x for x in range(len(files))]
    file_indices.reverse()
    i = 0
    print("start")
    while i < len(files) - 1:
        restart_cnt = False
        file = files[i]
        next_file = files[i+1]
        # print_data(data)
        # print()
        for ind in file_indices:
            last_file = files[ind]
            free_size = next_file[0] - (file[0]+file[1])
            free_space_index = file[0] + file[1]
            if free_size >= last_file[1]:
                cnt = 0
                files[i] = (files[i][0], files[i][1]+last_file[1], files[i][2])
                restart_cnt = True
                for j in range(free_space_index, free_space_index + last_file[1]):
                    data[j] = last_file[2]
                    data[last_file[0]+cnt] = -1
                    cnt += 1
                file_indices.remove(ind)
                break
        if restart_cnt:
            i = 0
        else:
            i += 1
        
    sum = 0
    # print_data(data)
    for i, c in enumerate(data):
        if c == -1:
            continue
        sum += i * int(c)

    return sum

start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")
