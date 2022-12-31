from typing import *
from collections import deque


def read_file():
    f = open("input.txt", "r")
    blueprints = []
    for line in f:
        blueprint = []
        s = line.strip()
        parts = s.split()
        blueprint.append(int(parts[6]))
        blueprint.append(int(parts[12]))
        blueprint.append([int(parts[18]), int(parts[21])])
        blueprint.append([int(parts[27]), int(parts[30])])
        blueprints.append(blueprint)
    return blueprints


def get_combinations(blueprint, resources):
    combinations = []
    if resources[0] // blueprint[3][0] > 0 and resources[2] // blueprint[3][1] > 0:
        combinations.append((0, 0, 0, 1))
        return combinations
    if resources[0] // blueprint[2][0] > 0 and resources[1] // blueprint[2][1] > 0:
        combinations.append((0, 0, 1, 0))
        return combinations
    if resources[0] // blueprint[0] == 1:
        combinations.append((1, 0, 0, 0))
    if resources[0] // blueprint[1] == 1:
        combinations.append((0, 1, 0, 0))
    combinations.append((0, 0, 0, 0))
    return combinations


def use_blueprint(blueprint: List, t: int):
    global max_depth
    best = 0
    best_info = []

    tasks = deque()
    robots = [1, 0, 0, 0]
    resources = [0, 0, 0, 0]
    tasks.append((robots, resources, t))
    while len(tasks) > 0:
        robots, resources, t = tasks.popleft()
        # if t < max_depth:
        #     max_depth = t
        #     print(max_depth)
        if t == 0:
            if resources[3] > best:
                best = resources[3]
                best_info.append((robots, resources))
            continue

        for combination in get_combinations(blueprint, resources):
            next_robots = [robots[i] + combination[i] for i in range(4)]
            next_resources = [resources[0] + robots[0] - combination[0] * blueprint[0] - combination[1] * blueprint[1]
                              - combination[2] * blueprint[2][0] - combination[3] * blueprint[3][0],
                              resources[1] + robots[1] - combination[2] * blueprint[2][1],
                              resources[2] + robots[2] - combination[3] * blueprint[3][1],
                              resources[3] + robots[3]]
            tasks.append((next_robots, next_resources, t - 1))
    return best


if __name__ == "__main__":
    blueprints = read_file()
    max_depth = 32

    geodes = []
    for blueprint in blueprints:
        geodes.append(use_blueprint(blueprint, 24))
    print(sorted(geodes, reverse=True))
    total = 0
    for i in range(len(geodes)):
        total += (i + 1) * geodes[i]
    print("Part 1:", total)

    # geodes = []
    # for i in range(min(len(blueprints), 3)):
    #     blueprint = blueprints[i]
    #     geodes.append(use_blueprint(blueprint, 32))
    # total = 1
    # for i in range(len(geodes)):
    #     total *= geodes[i]
    # print("Part 2:", total)




