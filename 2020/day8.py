import copy


data = []
f = open("day8.txt", "r")
for line in f:
    data.append(line.strip().split())
# print(data)

f.close()


def solve(dat):
    def acc(do, accumulator, cnum):
        accumulator += do
        cnum += 1
        return accumulator, cnum

    def jmp(do, accumulator, cnum):
        cnum += do
        return accumulator, cnum

    def nop(accumulator, cnum):
        cnum += 1
        return accumulator, cnum

    accumulator = 0
    cnum = 0
    been = set()
    while True:
        if cnum == len(data):
            return True, accumulator
        elif cnum in been:
            return False, accumulator
        else:
            op = dat[cnum]
            rule = op[0]
            delt = int(op[1])
            been.add(cnum)
            if rule == 'acc':
                accumulator, cnum = acc(delt, accumulator, cnum)
            elif rule == 'jmp':
                accumulator, cnum = jmp(delt, accumulator, cnum)
            elif rule == 'nop':
                accumulator, cnum = nop(accumulator, cnum)


print("Part 1:", solve(data)[1])


for i in range(len(data)):
    ndat = copy.deepcopy(data)
    if ndat[i][0] == 'jmp':
        ndat[i][0] = 'nop'
    elif ndat[i][0] == 'nop':
        ndat[i][0] = 'jmp'
    else:
        continue
    sol = solve(ndat)
    if sol[0]:
        print("Part 2:", sol[1])

