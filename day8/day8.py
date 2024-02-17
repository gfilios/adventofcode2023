import string


def read_input(filename):
    graph = {}
    with open(filename) as f:
        line = f.readline().strip('\n')
        steps = line.replace('L', '0').replace('R', '1')
        line = f.readline().strip('\n')
        line = f.readline().strip('\n')
        while line:
            assignment = line.split("=")
            node = assignment[0].strip()
            targets = assignment[1].replace("(", "").replace(")", "")
            left_right = targets.split(",")
            left_right[0] = left_right[0].strip()
            left_right[1] = left_right[1].strip()
            graph[node] = left_right
            line = f.readline().strip('\n')
    return steps, graph


def part1():
    steps, graph = read_input("input.txt")
    zzz_found = False
    step_counter = 0
    next_node = "AAA"
    while not zzz_found:
        for step in steps:
            step_counter += 1
            current_node = graph[next_node]
            next_node = current_node[int(step)]
            if next_node == "ZZZ":
                zzz_found = True
                break
    return step_counter


print(f"{part1()}")
