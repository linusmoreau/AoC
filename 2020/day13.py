

f = open("day13.txt", 'r')
beg = int(f.readline())
buses = f.readline().strip().split(',')

f.close()

# print(beg, buses)

ids = []
best_to = None
best = None
for bus in buses:
    if bus == 'x':
        ids.append(False)
        continue
    else:
        bus = int(bus)
        ids.append(bus)
        to = bus - beg % bus
        if best_to is None or to < best_to:
            best_to = to
            best = bus
        # timeto[bus] = to
# print(best, best_to)
print("Part 1:", best * best_to)


# print(ids)
# mult = max(ids)
# rel = buses.index(str(mult))
# print(mult, rel, s)
# n = mult - rel
# while True:
#     for i, bus in enumerate(ids):
#         if bus is not False:
#             val = n + i
#             # print(bus, n, rel, i)
#             if val % bus != 0:
#                 n += mult
#                 break
#     else:
#         break
# print("Part 2:", n)


# print(mult, rel)

# def solve(n, mult, ids):
#


n = 0
mult = None
its = ids
best = 1
while True:
    for i, bus in enumerate(its):
        if bus is not False:
            if mult is None:
                mult = bus
                n = mult
            if (n + i) % bus != 0:
                if i > best:
                    mult = 1
                    for m in its[:i]:
                        if m:
                            mult *= m
                    best = i
                n += mult
                break
    else:
        break

print("Part 2:", n)

