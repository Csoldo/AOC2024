import time
from copy import deepcopy

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/12.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")
    return lines

def flood(i, j, data, cluster: list, visited):
    cluster.append((i,j))
    visited[i][j] = True
    #up
    if i > 0 and data[i][j] == data[i-1][j] and not visited[i-1][j]:
        cluster, visited = flood(i-1, j, data, cluster, visited)
    #down
    if i < len(data) - 1 and data[i][j] == data[i+1][j] and not visited[i+1][j]:
        cluster, visited = flood(i+1, j, data, cluster, visited)
    #left
    if j > 0 and data[i][j] == data[i][j-1] and not visited[i][j-1]:
        cluster, visited = flood(i, j-1, data, cluster, visited)
    #right
    if j < len(data[0]) - 1 and data[i][j] == data[i][j+1] and not visited[i][j+1]:
        cluster, visited = flood(i, j+1, data, cluster, visited)
    
    return cluster, visited 


def calculate_perimeter(points: list, data):
    perimeter = 0
    for (i, j) in points:
        curr = data[i][j]
        # print(f"point: {i}, {j}, per: {perimeter}")
        if i in [0, len(data) - 1]:
            perimeter += 1
        if j in [0, len(data[0]) - 1]:
            perimeter += 1
        if i > 0 and curr != data[i-1][j]:
            perimeter += 1
        if j > 0 and curr != data[i][j-1]:
            perimeter += 1
        if i < len(data) - 1 and curr != data[i+1][j]:
            perimeter += 1
        if j < len(data[0]) - 1 and curr != data[i][j+1]:
            perimeter += 1
        # print(f"point: {i}, {j}, per: {perimeter}")
    return perimeter

def first_part():
    data = read_input()
    row_size = len(data)
    col_size = len(data[0])
    visited = [[False for x in line] for line in data]
    clusters = []
    for i in range(row_size):
        for j in range(col_size):
            if not visited[i][j]:
                current_clusters, visited = flood(i, j, data, [], visited)
                clusters.append({data[i][j]: current_clusters})
    sum = 0
    for cluster in clusters:
        for key, values in cluster.items():
            area = len(values)
            perimeter = calculate_perimeter(values, data)
            sum += area * perimeter

    return sum


start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")
