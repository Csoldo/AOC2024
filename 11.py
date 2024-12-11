import time
from copy import deepcopy

def read_input():
    input_file = "inputs/example.in"
    # input_file = "inputs/11.in"
    with open(input_file) as f:
        lines = f.read()
    data = lines.split()
    return [int(x) for x in data]

def transform(stone: int):
    if stone == 0:
        return [1]
    elif len(str(stone)) % 2 == 0:
        tmp = str(stone)
        return [int(tmp[:len(tmp) // 2]), int(tmp[len(tmp) // 2:])]
    else:
        stone = stone * 2024
        return [stone]

def first_part():
    stones = read_input()
    new_stones = deepcopy(stones)
    for _ in range(25):
        stones_list = []
        for stone in new_stones:
            for transformed in transform(stone):
                stones_list.append(transformed)
        new_stones = deepcopy(stones_list)
    return len(new_stones)


def second_part():
    stones = read_input()
    new_stones = deepcopy(stones)
    for i in range(75):
        print(f"starting blinking: {i}, length: {len(new_stones)}")
        print(len(stones))
        stones_list = []
        for stone in new_stones:
            for transformed in transform(stone):
                stones_list.append(transformed)
        new_stones = deepcopy(stones_list)
    return len(new_stones)


start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")


start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")
