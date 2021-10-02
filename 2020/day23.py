import numpy

data = []
f = open("day23.txt")
for line in f:
    for c in line:
        data.append(int(c))

f.close()

# print(data)


def move(pos, mini=None, maxi=None):
    def select_dest(dest):
        if dest in picked:
            return dest - 1
        elif dest < mini:
            return maxi
        else:
            return dest

    cur = pos.pop(0)
    picked = [pos.pop(0) for _ in range(3)]

    dest = cur - 1

    while True:
        ndest = select_dest(dest)
        if ndest == dest:
            break
        else:
            dest = ndest

    loc = pos.index(dest)

    res = pos[:loc + 1]
    res.extend(picked)
    res.extend(pos[loc + 1:])
    res.append(cur)
    return res




# pos = data.copy() + [max(data) + i + 1 for i in range(1000000 - len(data))]

