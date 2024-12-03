import time

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/3.in"
    with open(input_file) as f:
        lines = f.read()

    return lines

def parse_mul(data, index):
    i = index + 4
    mul_body = ""
    max = len(data)
    result = 1
    while data[i] != ')':
        mul_body += data[i]
        if i == max - 1 or i - index > 11:
            return i, 0
        i += 1
        
    mul_body = mul_body.split(",")
    try:
        a = int(mul_body[0])
        b = int(mul_body[1])
    except ValueError:
        return i, 0
    except IndexError:
        return i, 0
    result = a * b
    return i, result


def first_part():
    data = read_input()
    sum = 0
    for i in range(len(data)):
        if data[i] == 'm' and data[i:i+4] == "mul(":
            index, result = parse_mul(data, i)
            i = index
            sum += result
    
    return sum

def second_part():
    data = read_input()
    sum = 0
    enabled = True
    for i in range(len(data)):
        if data[i] == 'm' and data[i:i+4] == "mul(":
            index, result = parse_mul(data, i)
            i = index
            if enabled:
                sum += result
        
        elif data[i] == 'd' and data[i:i+7] == "don't()":
            i = i+7
            enabled = False
        elif data[i] == 'd' and data[i:i+4] == "do()":
            enabled = True
            i = i + 4

    return sum

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
