
rules = {}
nticks = []
mtick = None

r = True
m = False
n = False
f = open('day16.txt', 'r')
for line in f:
    if m:
        if line == 'nearby tickets:\n':
            n = True
            m = False
        elif line == '\n':
            continue
        else:
            mtick = [int(n) for n in line.strip().split(',')]
    elif n:
        nticks.append([int(n) for n in line.strip().split(',')])
    elif r:
        if line == 'your ticket:\n':
            m = True
            r = False
        elif line == '\n':
            continue
        else:
            dat = line.strip().split(': ')
            key = dat[0]
            temp = dat[1].split(' or ')
            val = []
            for v in temp:
                a = v.split('-')
                val.append(range(int(a[0]), int(a[1]) + 1))
            rules[key] = val

f.close()

# print(rules)
all_ranges = []
for val in rules.values():
    all_ranges.extend(val)
# print(all_ranges)
# print(mtick)
# print(nticks)


def in_ranges(n, ranges):
    for r in ranges:
        if n in r:
            return True
    else:
        return False


tot = 0
nnticks = nticks.copy()
for t in nticks:
    for n in t:
        if not in_ranges(n, all_ranges):
            tot += n
            try:
                nnticks.remove(t)
            except ValueError:
                pass
print("Part 1:", tot)

# print(len(nnticks))
results = {}
poss = {}
for rule in rules.keys():
    poss[rule] = list(range(len(rules)))
while len(results) < len(rules):
    for t in nnticks:
        for i, n in enumerate(t):
            for rule in poss.keys():
                rs = rules[rule]
                for r in rs:
                    if n in r:
                        break
                else:
                    try:
                        poss[rule].remove(i)
                    except ValueError:
                        pass
                if len(poss[rule]) == 1:
                    a = poss[rule][0]
                    results[rule] = mtick[a]
                    for r in poss.keys():
                        try:
                            poss[r].remove(a)
                        except ValueError:
                            pass

# print(results)
tot = 1
for r, n in results.items():
    if "departure" in r:
        tot *= n
print("Part 2:", tot)
