
data = []
f = open("day24.txt", "r")
for line in f:
    data.append(line.strip())


flipped = set()


def reform(order):
    dr = {}
    i = 0
    while i < len(order):
        c = order[i]
        if c in 'sn':
            try:
                dr[c + order[i + 1]] += 1
            except KeyError:
                dr[c + order[i + 1]] = 1
            i += 2
        else:
            try:
                dr[c] += 1
            except KeyError:
                dr[c] = 1
            i += 1
    return dr


def simplify(order):
    coord = [0, 0]
    if 'nw' in order:
        coord[0] -= order['nw']
        coord[1] -= order['nw']
    if 'sw' in order:
        coord[0] -= order['sw']
        coord[1] += order['sw']
    if 'ne' in order:
        coord[0] += order['ne']
        coord[1] -= order['ne']
    if 'se' in order:
        coord[0] += order['se']
        coord[1] += order['se']
    if 'w' in order:
        coord[0] -= order['w'] * 2
    if 'e' in order:
        coord[0] += order['e'] * 2
    return tuple(coord)


for order in data:
    target = simplify(reform(order))
    if target in flipped:
        flipped.remove(target)
    else:
        flipped.add(target)

print("Part 1:", len(flipped))


def neighbours(tile):
    nghb = ((tile[0] - 2, tile[1]),
            (tile[0] + 2, tile[1]),
            (tile[0] - 1, tile[1] - 1),
            (tile[0] - 1, tile[1] + 1),
            (tile[0] + 1, tile[1] - 1),
            (tile[0] + 1, tile[1] + 1))
    return nghb


def day(flipped):
    zone = {}
    for tile in flipped:
        nghb = neighbours(tile)
        for n in nghb:
            try:
                zone[n] += 1
            except KeyError:
                zone[n] = 1
    nflipped = set()
    for tile in flipped:
        if tile in zone and zone[tile] < 2:
            nflipped.add(tile)
    for tile in list(zone.keys()):
        if zone[tile] == 2:
            nflipped.add(tile)
    return nflipped


for d in range(100):
    flipped = day(flipped)
print("Part 2:", len(flipped))



