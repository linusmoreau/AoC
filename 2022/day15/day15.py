
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def in_range(sensor, beacon, p):
    return manhattan_distance(sensor, beacon) >= manhattan_distance(sensor, p)


def overlap(r1, r2):
    return r2[0] - 1 <= r1[0] <= r2[1] + 1 or r2[0] - 1 <= r1[1] <= r2[1] + 1 or \
           r1[0] - 1 <= r2[0] <= r1[1] or r1[0] - 1 <= r2[1] <= r1[1] + 1


def merge(r1, r2):
    if r1[0] < r2[0]:
        bottom = r1[0]
    else:
        bottom = r2[0]
    if r1[1] > r2[1]:
        top = r1[1]
    else:
        top = r2[1]
    return bottom, top


def merge_ranges(ranges):
    nranges = set()
    ranges = list(ranges)
    for i in range(len(ranges)):
        for j in range(i, len(ranges)):
            if overlap(ranges[i], ranges[j]):
                nranges.add(merge(ranges[i], ranges[j]))
                break
        else:
            nranges.add(ranges[i])
    return nranges


def read_file():
    f = open("input.txt", "r")
    pairs = []
    sensors = []
    beacons = []
    for line in f:
        s = line.strip()
        sensor_part, beacon_part = s.split(":")
        sensor_x = int(sensor_part[sensor_part.find("x=") + 2:sensor_part.find(",")])
        sensor_y = int(sensor_part[sensor_part.find("y=") + 2:])
        beacon_x = int(beacon_part[beacon_part.find("x=") + 2:beacon_part.find(",")])
        beacon_y = int(beacon_part[beacon_part.find("y=") + 2:])
        sensor = (sensor_x, sensor_y)
        beacon = (beacon_x, beacon_y)
        pairs.append((sensor, beacon))
        sensors.append(sensor)
        beacons.append(beacon)
    f.close()
    return pairs, sensors, beacons


if __name__ == "__main__":
    row = 10
    pairs, sensors, beacons = read_file()
    # leftmost = None
    # rightmost = None
    # for pair in pairs:
    #     r = manhattan_distance(pair[0], pair[1])
    #     left = pair[0][0] - r
    #     right = pair[0][0] + r
    #     if leftmost is None or left < leftmost:
    #         leftmost = left
    #     if rightmost is None or right > rightmost:
    #         rightmost = right

    # count = 0
    # print(leftmost, rightmost + 1)
    # for x in range(leftmost, rightmost + 1):
    #     if x % 100000 == 0:
    #         print(count)
    #     for p in pairs:
    #         if in_range(p[0], p[1], (x, row)) and (x, row) not in beacons:
    #             count += 1
    #             break
    # print("Part 1:", count)

    all_ranges = []
    for y in range(4000001):
        if y % 100000 == 0:
            print(y)
        ranges = []
        for pair in pairs:
            sensor = pair[0]
            beacon = pair[1]
            d = manhattan_distance(sensor, beacon)
            if sensor[1] - d <= y <= sensor[1]:
                x = y - (sensor[1] - d)
            elif sensor[1] <= y <= sensor[1] + d:
                x = sensor[1] + d - y
            else:
                continue
            r = (sensor[0] - x, sensor[0] + x)
            if r[1] < 0 or r[0] > 4000000:
                continue
            if len(ranges) == 0 or r[0] > ranges[-1][1]:
                ranges.append(r)
            elif r[1] < ranges[0][0]:
                ranges.insert(0, r)
            else:
                for i in range(len(ranges)):
                    c = ranges[i]
                    if overlap(c, r):
                        ranges[i] = merge(c, r)
                        if i > 0 and overlap(ranges[i - 1], ranges[i]):
                            ranges[i - 1] = merge(ranges[i], ranges[i - 1])
                            ranges.pop(i)
                        elif i + 1 < len(ranges) and overlap(ranges[i + 1], ranges[i]):
                            ranges[i] = merge(ranges[i + 1], ranges[i])
                            ranges.pop(i + 1)
                        break
                    elif i + 1 < len(ranges) and r[0] > c[1] and r[1] < ranges[i + 1][0]:
                        ranges.insert(i + 1, r)
                        break
        if len(ranges) == 2:
            if ranges[1][0] - ranges[0][1] == 2:
                print((ranges[1][0] - 1, y))
                break




