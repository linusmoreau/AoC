
def priority(c):
    p = ord(c.lower()) - 96
    if c != c.lower():
        p += 26
    return p


if __name__ == "__main__":
    rucksacks = []
    f = open("input.txt", "r")
    for line in f:
        s = line.strip()
        rucksacks.append(s)
    f.close()

    total = 0
    for rucksack in rucksacks:
        c1 = rucksack[:len(rucksack) // 2]
        c2 = rucksack[len(rucksack) // 2:]
        for c in c1:
            if c in c2:
                total += priority(c)
                break
    print("Part 1:", total)

    total = 0
    i = 0
    while i < len(rucksacks):
        found = False
        for c in rucksacks[i]:
            for d in rucksacks[i+1]:
                if c == d and c in rucksacks[i+2]:
                    total += priority(c)
                    i += 3
                    found = True
                    break
            if found:
                break
    print("Part 2:", total)


