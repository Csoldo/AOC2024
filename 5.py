import time

def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/5.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")
    rules = []
    read_rules = True
    updates = []
    for line in lines:
        if line == "":
            read_rules = False
            continue
        if read_rules:
            tmp = line.split("|")
            rules.append((int(tmp[0]), int(tmp[1])))
        else:
            tmp = line.split(",")
            updates.append([int(x) for x in tmp])
    
    return rules, updates

asd, x = read_input()

def indices(a: list, x: int):
    res = []
    for i in range(len(a)):
        item = a[i]
        if x == item:
            res.append(i)
    return res


def first_part():
    rules, updates = read_input()
    sum = 0
    for update in updates:
        is_valid_order = True
        for (a,b) in rules:
            if a in update and b in update:
                is_valid_order = update.index(a) < update.index(b)
            
            if not is_valid_order:
                break
        
        if is_valid_order:
            sum += update[len(update)//2]
            
    return sum

def second_part():
    rules, updates = read_input()
    sum = 0
    for update in updates:
        is_valid_order = True
        i = 0
        while i < (len(rules)):
            (a,b) = rules[i]
            if a in update and b in update:
                valid = update.index(a) < update.index(b)
                if not valid:
                    update[update.index(a)] = b
                    update[update.index(b)] = a
                    is_valid_order = False
                    i = 0
            i += 1

        if not is_valid_order:
            sum += update[len(update)//2]
            
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

