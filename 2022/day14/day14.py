
def read_file():
    f = open("input.txt", "r")
    rocks = set()
    lowest = 0
    for line in f:
        prev = None
        s = line.strip()
        vertices = s.split(" -> ")
        for v in vertices:
            t = v.split(",")
            vertex = (int(t[0]), int(t[1]))
            if vertex[1] > lowest:
                lowest = vertex[1]
            if prev is not None:
                if prev[0] == vertex[0]:
                    for y in range(min(prev[1], vertex[1]), max(prev[1], vertex[1]) + 1):
                        rocks.add((prev[0], y))
                elif prev[1] == vertex[1]:
                    for x in range(min(prev[0], vertex[0]), max(prev[0], vertex[0]) + 1):
                        rocks.add((x, prev[1]))
                else:
                    raise Exception("unexpected vertices")
            prev = vertex
    f.close()
    return rocks, lowest


def drop_sand(filled, orig, lowest):
    count = 0
    loc = orig
    while True:
        if loc[1] > lowest:
            return count
        if (loc[0], loc[1] + 1) not in filled:
            loc = (loc[0], loc[1] + 1)
        elif (loc[0] - 1, loc[1] + 1) not in filled:
            loc = (loc[0] - 1, loc[1] + 1)
        elif (loc[0] + 1, loc[1] + 1) not in filled:
            loc = (loc[0] + 1, loc[1] + 1)
        else:
            filled.add(loc)
            count += 1
            loc = orig


def drop_sand_with_floor(filled, orig, lowest):
    count = 0
    loc = orig
    while True:
        if loc[1] == lowest + 1:
            filled.add(loc)
            count += 1
            loc = orig
        elif (loc[0], loc[1] + 1) not in filled:
            loc = (loc[0], loc[1] + 1)
        elif (loc[0] - 1, loc[1] + 1) not in filled:
            loc = (loc[0] - 1, loc[1] + 1)
        elif (loc[0] + 1, loc[1] + 1) not in filled:
            loc = (loc[0] + 1, loc[1] + 1)
        else:
            if loc == orig:
                return count + 1
            filled.add(loc)
            count += 1
            loc = orig


if __name__ == "__main__":
    filled, lowest = read_file()
    print("Part 1:", drop_sand(filled.copy(), (500, 0), lowest))
    print("Part 2:", drop_sand_with_floor(filled.copy(), (500, 0), lowest))



