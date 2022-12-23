import ast
from functools import cmp_to_key


def compare(a, b):
    if type(a) is int and type(b) is int:
        if a == b:
            return 0
        elif a < b:
            return -1
        else:
            return 1
    elif type(a) is int:
        return compare([a], b)
    elif type(b) is int:
        return compare(a, [b])
    else:
        i = 0
        while True:
            if len(a) <= i and len(b) <= i:
                return 0
            elif len(a) <= i:
                return -1
            elif len(b) <= i:
                return 1
            else:
                result = compare(a[i], b[i])
                if result != 0:
                    return result
                i += 1


def parse_packet(p):
    return ast.literal_eval(p)


def read_file():
    f = open("input.txt", "r")
    pairs = []
    packets = []
    pair = []
    for line in f:
        s = line.strip()
        if len(s) == 0:
            continue
        p = parse_packet(s)
        pair.append(p)
        packets.append(p)
        if len(pair) == 2:
            pairs.append(pair)
            pair = []
    f.close()
    return pairs, packets


if __name__ == "__main__":
    pairs, packets = read_file()
    total = 0
    for i, pair in enumerate(pairs):
        if compare(pair[0], pair[1]) == -1:
            total += i + 1
    print("Part 1:", total)

    packets.append([[2]])
    packets.append([[6]])
    key = cmp_to_key(compare)
    sorted_packets = sorted(packets, key=key)
    print("Part 2:", (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))


