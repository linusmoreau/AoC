from math import log2

data = []
f = open("day14.txt", 'r')
for line in f:
    dat = line.strip().split()
    typ = dat[0]
    val = dat[2]
    if typ != 'mask':
        typ = int(typ[typ.find('[') + 1:-1])
        val = int(val)
    data.append((typ, val))

f.close()
# print(data)


def to_binary(n):
    s = ''
    c = None
    while True:
        mag = int(log2(n))
        n -= 2 ** mag
        if c is not None:
            s += '0' * (c - mag - 1)
        s += '1'
        if n == 0:
            s += '0' * mag
            break
        else:
            c = mag
    return s


def to_decimal(s):
    n = 0
    mag = len(s) - 1
    for b in s:
        if b == '1':
            n += 2 ** mag
        mag -= 1
    return n


def do_mask(val, mask):
    length = len(mask)
    v = to_binary(val).rjust(length, '0')
    fin = ''
    for i in range(length):
        if mask[i] == 'X':
            fin += v[i]
        else:
            fin += mask[i]
    return to_decimal(fin)


mem = {}
mask = None
for typ, val in data:
    if typ == 'mask':
        mask = val
        # print(mask)
    else:
        mem[typ] = do_mask(val, mask)
        # print(mem)

print("Part 1:", sum(mem.values()))


# Part 2


def get_dest(val, mask):
    length = len(mask)
    v = to_binary(val).rjust(length, '0')
    fin = ''
    for i in range(length):
        if mask[i] == '0':
            fin += v[i]
        else:
            fin += mask[i]
    return fin


def get_dests(dest):
    loc = dest.find('X')
    if loc == -1:
        return [to_decimal(dest)]
    else:
        return (get_dests(dest[:loc] + '0' + dest[loc + 1:]) +
                get_dests(dest[:loc] + '1' + dest[loc + 1:]))


mem = {}
mask = None
for typ, val in data:
    if typ == 'mask':
        mask = val
        # print(mask)
    else:
        dest = get_dest(typ, mask)
        dests = get_dests(dest)
        # print(dests)
        for d in dests:
            mem[d] = val
        # print(mem)

print("Part 2:", sum(mem.values()))
# print(to_binary(100))
