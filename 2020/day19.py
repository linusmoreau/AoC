import re


rules = {}
f = open("day19.txt", "r")

mssgs = []
reading_rules = True

for line in f:
    if len(line) == 1:
        reading_rules = False
        continue
    if reading_rules:
        inp = line.strip('\n').split(': ')
        rules[inp[0]] = inp[1]
    else:
        mssgs.append(line.strip('\n'))

# Part 1

resolved = {}
while '0' not in resolved.keys():
    for n, rule in rules.items():
        if rule[0] == '\"':
            resolved[n] = rule[1]
        parts = rule.split()
        for part in parts:
            if part == '|':
                continue
            if part not in resolved:
                break
        else:
            r = ""
            for part in parts:
                if part == '|':
                    r += '|'
                else:
                    r += resolved[part]
            resolved[n] = '(' + r + ')'

count = 0
for mssg in mssgs:
    if re.fullmatch(resolved['0'], mssg):
        count += 1
print("For part 1:", count)


# Part 2

rules['8'] = '42 | 42 8'
rules['11'] = '42 31 | 42 11 31'

seen = set()
while True:
    added = False
    for n, rule in rules.items():
        if rule[0] == '\"':
            resolved[n] = rule[1]
        parts = rule.split()
        for part in parts:
            if part == '|':
                continue
            if part not in resolved:
                break
        else:
            r = ""
            for part in parts:
                if part == '|':
                    r += '|'
                else:
                    r += resolved[part]
            resolved[n] = '(' + r + ')'

    for mssg in mssgs:
        if re.fullmatch(resolved['0'], mssg):
            if mssg not in seen:
                seen.add(mssg)
                added = True
    if not added:
        print("For part 2:", len(seen))
        break



