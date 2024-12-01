def read_input():
    input_file = "inputs/example.in"
    input_file = "inputs/1.in"
    with open(input_file) as f:
        lines = f.read()

    lines = lines.split("\n")

    left_list = []
    right_list = []
    for line in lines:
        tmp = line.split()
        left_list.append(tmp[0])
        right_list.append(tmp[1])
    return left_list, right_list



def first_part():
    left_list, right_list = read_input()
    left_list.sort()
    right_list.sort()
    sum = 0
    for i in range(len(left_list)):
        sum += abs(int(left_list[i]) - int(right_list[i]))

    print("First part: ", sum)


def second_part():
    def num_of_occurences_sorted(x: int, list: list):
        cnt = 0
        for item in list:
            if item < x:
                continue
            elif item == x:
                cnt += 1
            else:
                return cnt
        return cnt

    left_list, right_list = read_input()
    right_list.sort()

    sum = 0
    for item in left_list:
        sum += int(item) * num_of_occurences_sorted(item, right_list)
    print("Second part:", sum)


first_part()
second_part()
