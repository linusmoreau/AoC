
class Elf:
    def __init__(self, food):
        self.food = food

    def total(self):
        return sum(self.food)


if __name__ == "__main__":
    elves = []
    f = open("input.txt", "r")
    food = []
    for line in f:
        s = line.strip()
        if len(s) == 0:
            elves.append(Elf(food))
            food = []
        else:
            food.append(int(s))
    f.close()

    print("Part 1:", max(map(Elf.total, elves)))
    print("Part 2:", sum(sorted(map(Elf.total, elves), reverse=True)[:3]))
