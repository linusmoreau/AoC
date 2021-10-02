

# Get data

data = {}
f = open("day7.txt", "r")
for line in f:
    bag = {}
    inf = line.strip().split()
    clr = inf[0] + inf[1]
    if inf[4] == 'no':
        cont = {}
    else:
        cont = {}
        for t in range(1, int(len(inf) / 4)):
            i = t * 4
            cont[inf[i + 1] + inf[i + 2]] = int(inf[i])
    data[clr] = cont

f.close()

print(data)


# Part 1:


def num_reach(t):
    do_reach = set()

    def can_reach(f):
        if f in do_reach:
            return True
        elif f == t:
            do_reach.add(f)
            return True
        else:
            for c in data[f].keys():
                if can_reach(c):
                    do_reach.add(f)
                    return True
            else:
                return False

    def is_valid(f):
        if f == t:
            return False
        else:
            return can_reach(f)

    return sum([is_valid(f) for f in data.keys()])


print("Part 1:", num_reach('shinygold'))


# Part 2:

def num_in_bag(b):
    num = 0
    for bag, n in data[b].items():
        num += n * (num_in_bag(bag) + 1)
    return num


print("Part 2:", num_in_bag("shinygold"))
