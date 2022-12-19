
class Range:
    def __init__(self, beg, end):
        self.beg = beg
        self.end = end

    def contains(self, r):
        return self.beg <= r.beg and self.end >= r.end

    def overlap(self, r):
        return (self.end >= r.beg >= self.beg) or (r.end >= self.beg >= r.beg)


if __name__ == "__main__":
    pairs = []
    f = open("input.txt", "r")
    for line in f:
        s = line.strip()
        p1, p2 = s.split(",")
        a1 = p1.split("-")
        a2 = p2.split("-")
        pairs.append((Range(int(a1[0]), int(a1[1])), Range(int(a2[0]), int(a2[1]))))
    f.close()

    total = 0
    for pair in pairs:
        if pair[0].contains(pair[1]) or pair[1].contains(pair[0]):
            total += 1
    print("Part 1:", total)

    total = 0
    for pair in pairs:
        if pair[0].overlap(pair[1]):
            total += 1
    print("Part 2:", total)
