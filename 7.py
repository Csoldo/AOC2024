import time

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/7.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")
    values = []
    operands = []
    for line in lines:
        line = line.split(":")
        values.append(int(line[0]))
        operands.append([int(x) for x in line[1].split()])

    return values, operands


def first_part():
    values, numbers = read_input()
    sum = 0

    for i, row in enumerate(numbers):
        target = values[i]
        def calculate(index, acc):
            if index >= len(row):
                return acc

            times = calculate(index+1, acc*row[index])

            plus = calculate(index+1, acc+row[index])
            
            return times if times == target else plus
        
        possible = calculate(1, row[0])
        if possible == target:
            sum += target
        
    return sum

start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")


def concat_numbers(a, b):
    return int(f"{a}{b}")

def second_part():
    values, numbers = read_input()
    sum = 0

    for i, row in enumerate(numbers):
        target = values[i]
        def calculate(index, acc):
            if index >= len(row):
                return acc

            times = calculate(index+1, acc*row[index])
            plus = calculate(index+1, acc+row[index])
            concat = calculate(index+1, concat_numbers(acc,row[index]))

            if times == target:
                return times
            elif plus == target:
                return plus
            else:
                return concat
            
        possible = calculate(1, row[0])
        if possible == target:
            sum += target
        
    return sum

start_time = time.perf_counter()
second = second_part()
end_time = time.perf_counter()
print("Second part:", second)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")
