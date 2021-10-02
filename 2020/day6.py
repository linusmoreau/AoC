
# Part 1:

data = []
f = open("day6.txt", "r")

group = set()
for line in f:
    ln = line.strip()
    if ln == '':
        data.append(group)
        group = set()
    else:
        for c in ln:
            group.add(c)
data.append(group)
f.close()

print("Part 1:", sum(map(len, data)))


# Part 2:

data = []
f = open("day6.txt", "r")

group = None
for line in f:
    ln = line.strip()
    if ln == '':
        data.append(group)
        group = None
    else:
        person = set()
        for c in ln:
            person.add(c)
        if group is None:
            group = person
        else:
            group.intersection_update(person)
data.append(group)
f.close()


print("Part 2:", sum(map(len, data)))

