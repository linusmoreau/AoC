# Get data

data = []
all_alg = set()
all_ing = set()
all_ing_dup = []
f = open("day21.txt", "r")
for line in f:
    dat = {}
    entry = line.strip()[:-1].split()
    bar = entry.index('(contains')
    ing = entry[:bar]
    all_ing_dup .extend(ing)
    all_ing.update(ing)
    alg = entry[bar + 1:]
    for i, a in enumerate(alg):
        alg[i] = a.strip(',')
    all_alg.update(alg)
    dat['ing'] = set(ing)
    dat['alg'] = set(alg)
    data.append(dat)
f.close()
# print(data)
# print(all_alg)
# print(all_ing)
# print(all_ing_dup)


# Part 1

safe = all_ing.copy()
for a in all_alg:
    cause = None
    for entry in data:
        if a in entry['alg']:
            if cause is None:
                cause = entry['ing'].copy()
            else:
                cause.intersection_update(entry['ing'])
    safe.difference_update(cause)

total = 0
for s in safe:
    total += all_ing_dup.count(s)
print("Part 1:", total)


# Part 2
guilty = {}     # key is allergen, value is cause
sus = []
for entry in data:
    nentry = {}
    poss = entry['ing']
    poss.difference_update(safe)
    nentry['ing'] = poss
    nentry['alg'] = entry['alg']
    sus.append(nentry)
# print(sus)

ing_left = all_ing.copy()
alg_left = all_alg.copy()
while len(alg_left) != 0:
    for a in alg_left.copy():
        suspect = ing_left.copy()
        for entry in data:
            if a in entry['alg']:
                suspect.intersection_update(entry['ing'])
        if len(suspect) == 1:
            ing = suspect.pop()
            guilty[a] = ing
            ing_left.remove(ing)
            alg_left.remove(a)
# print(guilty)

out = ""
order = sorted(list(guilty.keys()))
for a in order:
    out += guilty[a] + ','
out = out[:-1]
print(out)




