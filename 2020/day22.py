
data = {}
f = open("day22.txt", 'r')

cp = None
nums = []
for line in f:
    if "Player" in line:
        cp = int(line.strip().split()[1].strip(':'))
    elif line == '\n':
        data[cp] = nums
        nums = []
    else:
        nums.append(int(line.strip()))
if len(nums) != 0:
    data[cp] = nums
del cp
del nums
f.close()

# print(data)


def turn(d1, d2):
    c1 = d1.pop(0)
    c2 = d2.pop(0)
    if c1 > c2:
        d1.extend([c1, c2])
    elif c2 > c1:
        d2.extend([c2, c1])
    else:
        raise ValueError("Two compared cards cannot be equal")
    return d1, d2


def rcombat(d1, d2):
    mem = set()

    def rcturn(d1, d2):
        if (tuple(d1), tuple(d2)) in mem:
            return 1, d1, []
        else:
            mem.add((tuple(d1), tuple(d2)))
            c1 = d1.pop(0)
            c2 = d2.pop(0)
            if len(d1) >= c1 and len(d2) >= c2:
                w, td1, td2 = rcombat(d1[:c1], d2[:c2])
                if w == 1:
                    d1.extend([c1, c2])
                    return 1, d1, d2
                elif w == 2:
                    d2.extend([c2, c1])
                    return 2, d1, d2
                else:
                    raise ValueError("There must be a winner to rcombat")
            elif c1 > c2:
                d1.extend([c1, c2])
                return 1, d1, d2
            elif c2 > c1:
                d2.extend([c2, c1])
                return 2, d1, d2
            else:
                raise ValueError("Two compared cards cannot be equal")

    while True:
        if len(d1) == 0:
            return 2, d1, d2
        elif len(d2) == 0:
            return 1, d1, d2
        w, d1, d2 = rcturn(d1, d2)


def score(d):
    score = 0
    for i, n in enumerate(d):
        score += n * (len(d) - i)
    return score


d1 = data[1].copy()
d2 = data[2].copy()
while True:
    if len(d1) == 0:
        winner = d2
        break
    elif len(d2) == 0:
        winner = d1
        break
    else:
        d1, d2 = turn(d1, d2)
# print(winner)

print("Part 1:", score(winner))

d1 = data[1].copy()
d2 = data[2].copy()
# print(d1, d2)
w, d1, d2 = rcombat(d1, d2)
# print("Deck 1:", d1)
# print("Deck 2:", d2)
if w == 1:
    winner = d1
elif w == 2:
    winner = d2
else:
    raise ValueError("There must be a winner to rcombat")
print("Part 2:", score(winner))
