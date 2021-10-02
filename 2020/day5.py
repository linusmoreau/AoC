from math import log2

# Get the data

passes = []
f = open("day5.txt", "r")
for line in f:
    passes.append(line.strip())


# Part 1
rows = 128
cols = 8


def find_loc(code):
    lower = 0
    upper = rows - 1
    for i in range(int(log2(rows))):
        c = code[i]
        dif = int((upper - lower + 1) / 2)
        if c == "F":
            upper -= dif
        else:
            lower += dif
    assert lower == upper
    row = lower

    lower = 0
    upper = cols - 1
    for i in range(int(log2(rows)), len(code)):
        c = code[i]
        dif = int((upper - lower + 1) / 2)
        if c == "L":
            upper -= dif
        else:
            lower += dif
    assert lower == upper
    col = lower

    return row, col


def seat_id(coord):
    return coord[0] * 8 + coord[1]


id_nums = set()
for p in passes:
    id_nums.add(seat_id(find_loc(p)))
print("Part 1:", max(id_nums))


# Part 2:

ps = set(range(max(id_nums)))
ps.difference_update(id_nums)
np = set()
for p in ps:
    if p - 1 not in ps and p != 0:
        np.add(p)
print("Part 2:", np.pop())


