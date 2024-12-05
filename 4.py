import time

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/4.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")
    return lines

def first_part():
    sum = 0
    data = read_input()
    row_size = len(data[0])
    col_size = len(data)
    # Rows
    for row in data:
        for i in range(row_size):
            if i < row_size - 3:
                if row[i:i+4] == "XMAS":
                    sum += 1
            if i > 2:
                if row[i-3:i+1] == "SAMX":
                    sum += 1
    # Columns
    cols = []
    for i in range(col_size):
        cols.append("".join([row[i] for row in data]))
    for col in cols:
        for j in range(col_size):
            if j < col_size - 3:
                if col[j:j+4] == "XMAS":
                    sum += 1
            if j > 2:
                if col[j-3:j+1] == "SAMX":
                    sum += 1

    #diagonals
    for i in range(row_size):
        for j in range(col_size):
            #NW-SE and SE NW
            if i < row_size - 3 and j < col_size - 3:
                substr = ""
                for k in range(4):
                    substr += data[i+k][j+k]
                if substr == "XMAS":
                    sum += 1
            if i > 2 and j > 2:
                substr = ""
                for k in range(4):
                    substr += data[i-k][j-k]
                if substr == "XMAS":
                    sum += 1

            #NE-SW and SW-NE
            if i < row_size - 3 and j > 2:
                substr = ""
                for k in range(4):
                    substr += data[i+k][j-k]
                if substr == "XMAS":
                    sum += 1
            if i > 2 and j < col_size - 3:
                substr = ""
                for k in range(4):
                    substr += data[i-k][j+k]
                if substr == "XMAS":
                    sum += 1

    return sum


start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")

def second_part():
    sum = 0
    data = read_input()
    row_size = len(data[0])
    col_size = len(data)
    # Rows
    sum = 0
    for i in range(row_size):
        for j in range(col_size):
            if i > 0 and j > 0 and i < row_size - 1 and j < row_size - 1:
                char = data[i][j]
                up_left = data[i-1][j-1]
                up_right = data[i-1][j+1]
                down_left = data[i+1][j-1]
                down_right = data[i+1][j+1]
                if char == 'A':
                    if (
                        (
                            (up_left == "S" and down_right == "M")
                                or 
                            (up_left == "M" and down_right == "S")
                        )
                        and 
                        (
                            (up_right == "M" and down_left == "S")
                                or
                            (up_right == "S" and down_left == "M")
                        )
                        ):
                        sum += 1
    return sum


start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")

