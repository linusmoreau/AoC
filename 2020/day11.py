
occupied = set()
unoccupied = set()
floor = set()
f = open("day11.txt", 'r')
row = 0
y = 0
for y, line in enumerate(f):
    row = line.strip()
    for x, loc in enumerate(row):
        if loc == 'L':
            unoccupied.add((x, y))
        elif loc == '.':
            floor.add((x, y))
        elif loc == '#':
            occupied.add((x, y))

ROWS = y + 1
COLS = len(row)

f.close()

seats = occupied | unoccupied


def neighbours(coord):
    nghb = set()
    for x in range(-1, 2):
        for y in range(-1, 2):
            nghb.add((coord[0] + x, coord[1] + y))
    nghb.remove(coord)
    return nghb


def turn(occupied):
    nghb_occ = {}
    for seat in seats:
        for nghb in neighbours(seat):
            if nghb in occupied:
                try:
                    nghb_occ[seat] += 1
                except KeyError:
                    nghb_occ[seat] = 1
    for seat in seats:
        if seat not in occupied and seat not in nghb_occ.keys():
            occupied.add(seat)
        elif seat in occupied and seat in nghb_occ.keys() and nghb_occ[seat] >= 4:
            occupied.remove(seat)
    return occupied


pocc = None
occ = occupied.copy()
while True:
    occ = turn(occ)
    if pocc is not None and pocc == occ:
        break
    pocc = occ.copy()
print("Part 1:", len(occ))


def view(coord):
    def do(x, y, o):
        if (x, y) in seats:
            nghb.add((x, y))
            not_found.remove(o)
        if x < 0 or x > COLS or y < 0 or y > ROWS:
            not_found.remove(o)

    nghb = set()
    d = 0
    not_found = [i for i in range(8)]
    while len(not_found) != 0:
        d += 1
        for o in not_found.copy():
            if o == 0:
                x = coord[0] - d
                y = coord[1] - d
            elif o == 1:
                x = coord[0]
                y = coord[1] - d
            elif o == 2:
                x = coord[0] + d
                y = coord[1] - d
            elif o == 3:
                x = coord[0] - d
                y = coord[1]
            elif o == 4:
                x = coord[0] + d
                y = coord[1]
            elif o == 5:
                x = coord[0] - d
                y = coord[1] + d
            elif o == 6:
                x = coord[0]
                y = coord[1] + d
            else:
                x = coord[0] + d
                y = coord[1] + d
            do(x, y, o)
    return nghb


def nturn(occupied):
    nghb_occ = {}
    for seat in seats:
        for nghb in view(seat):
            if nghb in occupied:
                try:
                    nghb_occ[seat] += 1
                except KeyError:
                    nghb_occ[seat] = 1
    for seat in seats:
        if seat not in occupied and seat not in nghb_occ.keys():
            occupied.add(seat)
        elif seat in occupied and seat in nghb_occ.keys() and nghb_occ[seat] >= 5:
            occupied.remove(seat)
    return occupied


pocc = None
occ = occupied.copy()
while True:
    occ = nturn(occ)
    if pocc is not None and pocc == occ:
        break
    pocc = occ.copy()
print("Part 2:", len(occ))
