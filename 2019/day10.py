import math


def gcd(dividend, divisor):
    remainder = dividend % divisor
    if remainder == 0:
        return divisor
    else:
        return gcd(divisor, remainder)


def angle_ratio(h, v):
    if h != 0 and v != 0:
        if abs(v) > abs(h):
            gcf = gcd(abs(v), abs(h))
        else:
            gcf = gcd(abs(h), abs(v))
        v = v // gcf
        h = h // gcf
    elif h == 0:
        if v > 0:
            v = 1
        elif v < 0:
            v = -1
    elif v == 0:
        if h > 0:
            h = 1
        elif h < 0:
            h = -1
    return h, v


def gen_from_pos(asteroids, a):
    from_pos = {}
    for o in asteroids:
        if o == a:
            continue
        y_dif = o[1] - a[1]
        x_dif = o[0] - a[0]
        ratio = angle_ratio(x_dif, y_dif)
        if ratio in from_pos:
            value = from_pos[ratio]
            value.append(o)
            from_pos[ratio] = value
        else:
            from_pos[ratio] = [o]
    return from_pos


def order(pos):
    if pos[0] == 0:
        return -1000
    else:
        return math.atan(pos[1] / pos[0])


def dist(coord):
    return abs(best[0] - coord[0]) + abs(best[1] - coord[1])


received = []
f = open("day10_input.txt", "r")
for line in f:
    line_receive = []
    for char in line.strip():
        line_receive.append(char)
    received.append(line_receive)
f.close()

asteroids = []
for y in range(len(received)):
    for x in range(len(received[y])):
        sym = received[y][x]
        if sym == '#':
            asteroids.append((x, y))

best = None
largest = 0
for a in asteroids:
    from_pos = gen_from_pos(asteroids, a)
    num_in_sight = len(from_pos)
    if num_in_sight > largest:
        best = a
        largest = num_in_sight
# print(best, largest)
from_pos = gen_from_pos(asteroids, best)
for angle in from_pos:
    from_pos[angle].sort(key=dist)
quadrants = {1: [], 2: [], 3: [], 4: []}
for ratio in from_pos:
    quadrant = None
    if ratio[0] >= 0:
        if ratio[1] > 0:
            quadrant = 2
        elif ratio[1] <= 0:
            quadrant = 1
    elif ratio[0] < 0:
        if ratio[1] >= 0:
            quadrant = 3
        elif ratio[1] < 0:
            quadrant = 4
    quadrants[quadrant].append(ratio)

# print(len(quadrants[1]), len(quadrants[2]), len(quadrants[3]), len(quadrants[4]))
counter = 0
for quadrant in quadrants:
    quadrants[quadrant].sort(key=order)
    # print(quadrants[quadrant])
running = True
while running:
    for quadrant in range(1, 5):
        for shot in sorted(quadrants[quadrant], key=order):
            counter += 1
            # print(shot, end=" ")
            # print(from_pos[shot][0])
            if counter == 200 or counter == 199 or counter == 201:
                print(shot, end=" ")
                print(from_pos[shot][0])
                running = False
            from_pos[shot].pop(0)
            if len(from_pos[shot]) == 0:
                quadrants[quadrant].remove(shot)
    for quadrant in quadrants:
        if len(quadrants[quadrant]) != 0:
            break
    else:
        running = False

