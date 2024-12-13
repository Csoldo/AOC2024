import time

class Point:
    x: int
    y: int
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __str__(self):
        return f"(x, y)"

def get_values(line: str):
    tmp = line.split(":")[1]
    tmp = tmp.split(",")
    if "+" in tmp[0]: 
        x = tmp[0].split("+")[1]
        y = tmp[1].split("+")[1]
        return int(x), int(y)
    else:
        x = tmp[0].split("=")[1]
        y = tmp[1].split("=")[1]
        return int(x), int(y)


def read_input() -> [(Point, Point, Point)]: # type: ignore
    input_file = "inputs/example.in"
    input_file = "inputs/13.in"
    with open(input_file) as f:
        lines = f.read()
    data = lines.split("\n")
    
    result = []
    i = 0
    while i < len(data):
        if data[i] == "":
            continue
        x, y = get_values(data[i])
        button_a = Point(x, y)
        i += 1
        x, y = get_values(data[i])
        button_b = Point(x, y)
        i += 1
        x, y = get_values(data[i])
        prize = Point(x, y)
        i += 1
        result.append((button_a, button_b, prize))
        i += 1

    return result

def first_part():
    data = read_input()
    price = 0
    for (a, b, prize) in data:
        curr_price = 0
        for i in range(0, 100):
            for j in range(0, 100):
                xs = i * a.x + j * b.x
                ys = i * a.y + j * b.y
                if xs > prize.x or ys > prize.y:
                    break
                elif xs == prize.x and ys == prize.y:
                    curr_price = 3*i + j
                    break
            if curr_price > 0:
                break
        price += curr_price
    
    return price

start_time = time.perf_counter()
first = first_part()
end_time = time.perf_counter()
print("First part: ", first)
execution_time = (end_time - start_time) * 1000
print(f"Execution time: {execution_time:.4f} ms")
