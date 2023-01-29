from collections import deque


def read_file():
    f = open("input.txt", "r")
    cubes = set()
    for line in f:
        s = line.strip()
        parts = s.split(",")
        cube = (int(parts[0]), int(parts[1]), int(parts[2]))
        cubes.add(cube)
    f.close()
    return cubes


def adjacent(point):
    return ((point[0] - 1, point[1], point[2]),
            (point[0] + 1, point[1], point[2]),
            (point[0], point[1] - 1, point[2]),
            (point[0], point[1] + 1, point[2]),
            (point[0], point[1], point[2] - 1),
            (point[0], point[1], point[2] + 1))


def get_extremities(points):
    x_min = None
    x_max = None
    y_min = None
    y_max = None
    z_min = None
    z_max = None
    for p in points:
        if x_min is None or p[0] < x_min:
            x_min = p[0]
        if x_max is None or p[0] > x_max:
            x_max = p[0]
        if y_min is None or p[1] < y_min:
            y_min = p[1]
        if y_max is None or p[1] > y_max:
            y_max = p[1]
        if z_min is None or p[2] < z_min:
            z_min = p[2]
        if z_max is None or p[2] > z_max:
            z_max = p[2]
    return (x_min, x_max), (y_min, y_max), (z_min, z_max)


def get_shell(extremities):
    shell = set()
    for y in range(extremities[1][0] - 1, extremities[1][1] + 2):
        for z in range(extremities[2][0] - 1, extremities[2][1] + 2):
            shell.add((extremities[0][0] - 1, y, z))
            shell.add((extremities[0][1] + 1, y, z))
        for x in range(extremities[0][0] - 1, extremities[0][1] + 2):
            shell.add((x, y, extremities[2][0] - 1))
            shell.add((x, y, extremities[2][1] + 1))
    for z in range(extremities[2][0] - 1, extremities[2][1] + 2):
        for x in range(extremities[0][0] - 1, extremities[0][1] + 2):
            shell.add((x, extremities[1][0] - 1, z))
            shell.add((x, extremities[1][1] + 1, z))
    return shell


def part1(cubes):
    total = 0
    for cube in cubes:
        total += 6
        for c in adjacent(cube):
            if c in cubes:
                total -= 1
    return total


def part2(cubes):
    total = 0
    extremities = get_extremities(cubes)
    inner_shell = get_shell(extremities)
    outer_shell = get_shell((
        (extremities[0][0] - 1, extremities[0][1] + 1),
        (extremities[1][0] - 1, extremities[1][1] + 1),
        (extremities[2][0] - 1, extremities[2][1] + 1)))
    steam = inner_shell.union(outer_shell)
    todo = deque(inner_shell)
    while len(todo) > 0:
        cell = todo.pop()
        for c in adjacent(cell):
            if c in cubes:
                total += 1
            elif c not in steam:
                todo.append(c)
                steam.add(c)
    return total


if __name__ == "__main__":
    cubes = read_file()
    print("Part 1:", part1(cubes))
    print("Part 2:", part2(cubes))
