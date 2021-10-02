
f = open("day15.txt", "r")
data = [int(e) for e in f.readline().strip().split(',')]

f.close()

# print(data)


said = data.copy()
said.reverse()
turn = len(said)
while turn < 2020:
    try:
        i = said.index(said[0], 1)
        said = [i] + said
    except ValueError:
        said = [0] + said
    turn += 1
print("Part 1:", said[0])


# Part 2
said = data.copy()
turn = len(said)
seen = {}
for i, e in enumerate(said):
    seen[e] = i
while turn < 30000000:
    ith = turn - 1
    try:
        said.append(ith - seen[said[-1]])
    except KeyError:
        said.append(0)
    seen[said[-2]] = ith
    turn += 1
    # if turn % 1000000 == 0:
    #     print(turn)
print("Part 2:", said[-1])
