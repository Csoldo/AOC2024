import time
from typing import List

import matplotlib.pyplot as plt

class Robot:
    position_x: int
    position_y: int
    velocity_x: int
    velocity_y: int
    
    def __init__(self, position_x, position_y, velocity_x, velocity_y):
        self.position_x = position_x
        self.position_y = position_y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def __repr__(self):
        return f"({self.position_x},{self.position_y}) | ({self.velocity_x},{self.velocity_y})"

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/14.in"
    with open(input_file) as f:
        lines = f.read()
    
    data: List[Robot] = []
    for line in lines.split("\n"):
        line = line.split(" ")
        pos = line[0].split("=")[1].split(",")
        vel = line[1].split("=")[1].split(",")
        data.append(Robot(int(pos[0]), int(pos[1]), int(vel[0]), int(vel[1])))

    return data

def first_part():
    data = read_input()
    x_size = 101
    y_size = 103
    num_of_seconds = 10

    final_locations = [[0 for _ in range(x_size)] for _ in range(y_size)]

    for robot in data:
        final_x = (robot.position_x + robot.velocity_x * num_of_seconds) % x_size
        final_y = (robot.position_y + robot.velocity_y * num_of_seconds) % y_size
        
        final_locations[final_y][final_x] += 1

    # for row in final_locations:
    #     print(row)


    #quadrant one:

    safety_factor = 1
    offset_y = int(y_size / 2) + 1
    offset_x = int(x_size / 2) + 1
    quadrant_factor = 0
    #first quadrant
    for j in range(0, offset_y - 1):
        for i in range(0, offset_x - 1):
            quadrant_factor += final_locations[j][i]
    safety_factor *= quadrant_factor
    quadrant_factor = 0

    #second quadrant
    for j in range(offset_y, y_size):
        for i in range(0, offset_x - 1):
            quadrant_factor += final_locations[j][i]
    safety_factor *= quadrant_factor
    quadrant_factor = 0

    #third quadrant
    for j in range(0, offset_y - 1):
        for i in range(offset_x, x_size):
            quadrant_factor += final_locations[j][i]
    safety_factor *= quadrant_factor
    quadrant_factor = 0

    #fourth quadrant
    for j in range(offset_y, y_size):
        for i in range(offset_x, x_size):
            quadrant_factor += final_locations[j][i]
    safety_factor *= quadrant_factor

    return safety_factor

start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")    


def second_part():
    data = read_input()
    x_size = 101
    y_size = 103
    num_of_seconds_start = 6000
    num_of_seconds_end = 8000
    rows, cols = 10, 10
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 3, rows * 3))
    axes = axes.flatten()

    cnt = 0
    distinct_robot_cnt = 0
    for s in range(num_of_seconds_start, num_of_seconds_end):
        final_locations = [[0 for _ in range(x_size)] for _ in range(y_size)]
        for robot in data:
            final_x = (robot.position_x + robot.velocity_x * s) % x_size
            final_y = (robot.position_y + robot.velocity_y * s) % y_size
            
            if final_locations[final_y][final_x] == 0:
                final_locations[final_y][final_x] = 1
                distinct_robot_cnt += 1

        ax = axes[cnt]
        ax.imshow(final_locations, cmap='gray', interpolation='none')
        ax.set_title(f"Second {s}")
        ax.axis('off')
        cnt += 1

start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")
