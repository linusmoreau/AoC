
tiles = {}
f = open('day20.txt', 'r')
tile = []
n = None
for line in f:
    if 'Tile' in line:
        if n is not None:
            tiles[n] = tile
            tile = []
        n = int(line.strip().split()[1].strip(':'))
    elif len(line) > 1:
        tile.append(line.strip())
if n is not None:
    tiles[n] = tile

f.close()

# print(tiles)


def answer(corners):
    res = 1
    for c in corners:
        res *= c
    return res


def left(tile):
    c = ''
    for r in tile:
        c += r[0]
    return c


def right(tile):
    c = ''
    for r in tile:
        c += r[-1]
    return c


def matches(tn, tiles):
    tile = tiles[tn]
    m = {}
    for n, t in tiles.items():
        if n != tn:
            for i, tt in enumerate(orientations(t)):
                if tile[0] == tt[-1]:
                    m['top'] = n
                    break
                if tile[-1] == tt[0]:
                    m['bot'] = n
                    break
                if left(tile) == right(tt):
                    m['lef'] = n
                    break
                if right(tile) == left(tt):
                    m['rig'] = n
                    break
    return m


def match(tn, todo, tiles, data=None):
    tile = tiles[tn]
    if data is None:
        data = {}
    m = {}
    ntiles = tiles.copy()
    for n, t in tiles.items():
        if n != tn:
            for i, tt in enumerate(orientations(t)):
                if tile[0] == tt[-1]:
                    m['top'] = n
                    ntiles[n] = tt
                    break
                if tile[-1] == tt[0]:
                    m['bot'] = n
                    ntiles[n] = tt
                    break
                if left(tile) == right(tt):
                    m['lef'] = n
                    ntiles[n] = tt
                    break
                if right(tile) == left(tt):
                    m['rig'] = n
                    ntiles[n] = tt
                    break
    data[tn] = m
    # print(tn, m)
    todo.extend(list(m.values()))
    for do in todo.copy():
        if do in data:
            todo.remove(do)
    if len(todo) == 0:
        return data, ntiles
    return match(todo[0], todo[1:], ntiles, data)


def flip_horizontal(tile):
    t = []
    for r in tile:
        t.append(r[::-1])
    return t


def flip_vertical(tile):
    tile.reverse()
    return tile


def rotate(tile, times=1):
    if times == 0:
        return tile
    else:
        t = []
        for i in range(len(tile)):
            r = ''
            for j in range(len(tile)):
                r = tile[j][i] + r
            t.append(r)
        return rotate(t, times - 1)


def orientations(tile):
    def flips(tile):
        o = [tile.copy(), flip_vertical(tile.copy())]
        nt = flip_horizontal(tile.copy())
        o.append(nt.copy())
        o.append(flip_vertical(nt.copy()))
        return o

    o = []

    tt = tile.copy()
    o.extend(flips(tt))

    tt = rotate(tile.copy())
    o.extend(flips(tt))

    return o


def multiply(lon):
    tot = 1
    for n in lon:
        tot *= n
    return tot


def monsters(img):
    count = 0
    for img in orientations(img):
        for i in range(len(img) - 2):
            for j in range(len(img[i]) - 20):
                points = [img[i][j + 18],
                          img[i + 1][j],
                          img[i + 1][j + 5],
                          img[i + 1][j + 6],
                          img[i + 1][j + 11],
                          img[i + 1][j + 12],
                          img[i + 1][j + 17],
                          img[i + 1][j + 18],
                          img[i + 1][j + 19],
                          img[i + 2][j + 1],
                          img[i + 2][j + 4],
                          img[i + 2][j + 7],
                          img[i + 2][j + 10],
                          img[i + 2][j + 13],
                          img[i + 2][j + 16]]
                if '.' not in points:
                    count += 1
    return count


def expand_left(n, dat, data):
    r = [n]
    try:
        return r + expand_left(dat['lef'], data[dat['lef']], data)
    except KeyError:
        return r


def expand_right(n, dat, data):
    r = [n]
    try:
        return r + expand_right(dat['rig'], data[dat['rig']], data)
    except KeyError:
        return r


def expand_down(n, dat, data):
    try:
        r = [[n] + expand_right(dat['rig'], data[dat['rig']], data)]
    except KeyError:
        r = [[n] + expand_left(dat['lef'], data[dat['lef']], data)]
    try:
        r.extend(expand_down(dat['bot'], data[dat['bot']], data))
        return r
    except KeyError:
        return r


def expand_up(n, dat, data):
    try:
        r = [[n] + expand_right(dat['rig'], data[dat['rig']], data)]
    except KeyError:
        r = [[n] + expand_left(dat['lef'], data[dat['lef']], data)]
    try:
        r.extend(expand_up(dat['top'], data[dat['top']], data))
        return r
    except KeyError:
        return r


def expand(n, dat, data):
    if 'top' in dat:
        return expand_up(n, dat, data)
    else:
        return expand_down(n, dat, data)


def strip_sides(img):
    nimg = []
    for i in range(1, len(img) - 1):
        nimg.append(img[i][1:len(img) - 1])
    return nimg


todo = list(tiles.keys())
first = todo[0]
data, tiles = match(first, [], tiles)
# print(data)

corners = []
for n in tiles:
    m = matches(n, tiles)
    if len(m.values()) == 2:
        corners.append(n)
print("Part 1:", multiply(corners))

ndat = None
# print(data)
for tr in data.keys():
    v = data[tr]
    if len(v) == 2 and "bot" in v and "rig" in v:
        ndat = expand(tr, data[tr], data)
        break

# print(ndat)
for i, r in enumerate(ndat):
    for j, n in enumerate(r):
        ndat[i][j] = strip_sides(tiles[n])
        # ndat[i][j] = tiles[n]
# for r in ndat:
#     for b in r:
#         print(b)

img = []
for r in ndat:
    for i in range(len(r[0])):
        line = ''
        for s in r:
            line += s[i]
        img.append(line)
        # print(line)

size = 15
img_test = [".#.#..#.##...#.##..#####",
            "###....#.#....#..#......",
            "##.##.###.#.#..######...",
            "###.#####...#.#####.#..#",
            '##.#....#.##.####...#.##',
            '...########.#....#####.#',
            '....#..#...##..#.#.###..',
            '.####...#..#.....#......',
            '#..#.##..#..###.#.##....',
            '#.####..#.####.#.#.###..',
            '###.#.#...#.######.#..##',
            '#.####....##..########.#',
            '##..##.#...#...#.#.#.#..',
            '...#..#..#.#.##..###.###',
            '.#.#....#.##.#...###.##.',
            '###.#...#..#.##.######..',
            '.#.#.###.##.##.#..#.##..',
            '.####.###.#...###.#..#.#',
            '..#.#..#..#.#.#.####.###',
            '#..####...#.#.#.###.###.',
            '#####..#####...###....##',
            '#.##..#..#...#..####...#',
            '.#.###..##..##..####.##.',
            "...###...##...#...#..###"]
n = monsters(img)
# print(n)
print("Part 2:", sum([line.count('#') for line in img]) - n * size)
