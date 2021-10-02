


data = []
f = open("day10.txt", 'r')
for line in f:
    data.append(int(line.strip()))

f.close()

# print(data)
data.append(0)
data.append(max(data) + 3)
data.sort()
# print(data)

gaps = {}
for i in range(len(data) - 1):
    dif = data[i + 1] - data[i]
    try:
        gaps[dif] += [i + 1]
    except KeyError:
        gaps[dif] = [i + 1]
print("Part 1:", len(gaps[1]) * len(gaps[3]))

focal = [0] + gaps[3]
# print(data)
# print(focal)

# (0, 1, 2, 3, 4, 5)
found = {}


def ways(num):
    def find():
        w = 0
        if num == 1:
            return 1
        if num > 1:
            w += ways(num - 1)
        if num > 2:
            w += ways(num - 2)
        if num > 3:
            w += ways(num - 3)
        return w

    try:
        return found[num]
    except KeyError:
        finding = find()
        found[num] = finding
        return finding


tot = 1
for i in range(1, len(focal)):
    tot *= ways(focal[i] - focal[i - 1])
print("Part 2:", tot)

