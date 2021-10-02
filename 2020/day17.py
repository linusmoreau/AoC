
# Part 1

active = set()
f = open("day17.txt", "r")
for y, line in enumerate(f):
    for x, c in enumerate(line):
        if c == '#':
            active.add((x, y, 0))
f.close()


def gen_neighbours(coord):
    nghb = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                if x == y == z == 0:
                    continue
                else:
                    nghb.append((coord[0] + x, coord[1] + y, coord[2] + z))
    return nghb


def cycle(active):
    ofnote = {}
    for coord in active:
        for nc in gen_neighbours(coord):
            try:
                ofnote[nc] += 1
            except KeyError:
                ofnote[nc] = 1
    nactive = set()
    for coord, num in ofnote.items():
        if coord in active:
            if num == 2 or num == 3:
                nactive.add(coord)
        else:
            if num == 3:
                nactive.add(coord)
    return nactive


for i in range(6):
    active = cycle(active)
print("For part 1:", len(active))


# For part 2:

active = set()
f = open("day17.txt", "r")
for y, line in enumerate(f):
    for x, c in enumerate(line):
        if c == '#':
            active.add((x, y, 0, 0))


def gen_neighbours2(coord):
    nghb = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                for w in range(-1, 2):
                    if x == y == z == w == 0:
                        continue
                    else:
                        nghb.append((coord[0] + x, coord[1] + y, coord[2] + z, coord[3] + w))
    return nghb


def cycle2(active):
    ofnote = {}
    for coord in active:
        for nc in gen_neighbours2(coord):
            try:
                ofnote[nc] += 1
            except KeyError:
                ofnote[nc] = 1
    nactive = set()
    for coord, num in ofnote.items():
        if coord in active:
            if num == 2 or num == 3:
                nactive.add(coord)
        else:
            if num == 3:
                nactive.add(coord)
    return nactive


for i in range(6):
    active = cycle2(active)
print("For part 2:", len(active))
