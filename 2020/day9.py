
data = []
f = open('day9.txt', 'r')
for line in f:
    data.append(int(line.strip()))
# print(data)


SIZE = 25


def isvalid(num, prev):
    for i in range(len(prev) - 1):
        for j in range(i + 1, len(prev)):
            s = prev[i] + prev[j]
            if s == num:
                return True
    else:
        return False


num = None
for i in range(SIZE, len(data)):
    num = data[i]
    valid = isvalid(num, data[i - SIZE:i])
    if not valid:
        print("Part 1:", num)
        break


def solve(num, data):
    for i in range(len(data) - 1):
        tot = 0
        rec = []
        for j in range(i, len(data)):
            add = data[j]
            tot += add
            rec.append(add)
            if len(rec) > 1 and tot == num:
                return rec
            elif tot > num:
                break
    else:
        return False


solution = solve(num, data)
print("Part 2:", min(solution) + max(solution))



