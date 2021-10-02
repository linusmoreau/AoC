

def wire(path):
    wire_path = []
    loc = [0, 0]
    for ins in path:
        op = ins[0]
        num = int(ins[1:])
        if op == "R":
            for i in range(num):
                loc[0] += 1
                wire_path.append(tuple(loc))
        elif op == "L":
            for i in range(num):
                loc[0] -= 1
                wire_path.append(tuple(loc))
        elif op == "D":
            for i in range(num):
                loc[1] += 1
                wire_path.append(tuple(loc))
        elif op == "U":
            for i in range(num):
                loc[1] -= 1
                wire_path.append(tuple(loc))
    return wire_path


def trim(wire, wire_dist, index=0):
    wire = wire[:wire_dist]
    for i in range(index, len(wire) - 1):
        temp = wire[i+1]
        if wire[i] in temp:
            j = temp.index(wire[i])
            del wire[i:j]
            break
    return wire


def path_distance(point, wire1, wire2):
    wire1_dist = len(trim(wire1.copy(), wire1.index(point))) + 1
    wire2_dist = len(trim(wire2.copy(), wire2.index(point))) + 1
    return wire1_dist + wire2_dist


def crossover(wire1, wire2):
    cross_points = wire1.intersection(wire2)
    # smallest = 100000
    # for point in cross_points:
    #    if abs(point[0]) + abs(point[1]) < smallest:
    #        smallest = abs(point[0]) + abs(point[1])
    return cross_points


wires = []
f = open("day3_input.txt", "r")
for line in f:
    wires.append(line.split(","))
f.close()
wire1 = wire(wires[0])
wire2 = wire(wires[1])
cross_points = crossover(set(tuple(wire1)), set(tuple(wire2)))
smallest = -1
for point in cross_points:
    dist = path_distance(point, wire1, wire2)
    if dist < smallest or smallest == -1:
        smallest = dist
print("Final: " + str(smallest))
# print(crossover(set(tuple(wire1)), set(tuple(wire2))))


