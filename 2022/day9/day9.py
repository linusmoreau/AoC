
class Rope:
    def __init__(self):
        self.head = [0, 0]
        self.tail = [0, 0]
        self.been = {(0, 0)}

    def move(self, d, times):
        for i in range(times):
            if d == "L":
                self.head[0] -= 1
            elif d == "R":
                self.head[0] += 1
            elif d == "U":
                self.head[1] -= 1
            elif d == "D":
                self.head[1] += 1
            else:
                raise Exception
            self.move_tail()

    def move_tail(self):
        if abs(self.head[0] - self.tail[0]) > 1 or abs(self.head[1] - self.tail[1]) > 1:
            if self.head[0] > self.tail[0]:
                self.tail[0] += 1
            elif self.head[0] < self.tail[0]:
                self.tail[0] -= 1
            if self.head[1] > self.tail[1]:
                self.tail[1] += 1
            elif self.head[1] < self.tail[1]:
                self.tail[1] -= 1
            self.been.add((self.tail[0], self.tail[1]))


class LongRope(Rope):
    def __init__(self, length):
        super().__init__()
        self.knots = [[0, 0] for _ in range(length)]
        self.knots[0] = self.head
        self.knots[9] = self.tail

    def move_tail(self):
        for i in range(len(self.knots) - 1):
            self.move_together(self.knots[i], self.knots[i + 1])
        self.been.add((self.tail[0], self.tail[1]))

    @staticmethod
    def move_together(head, tail):
        if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
            if head[0] > tail[0]:
                tail[0] += 1
            elif head[0] < tail[0]:
                tail[0] -= 1
            if head[1] > tail[1]:
                tail[1] += 1
            elif head[1] < tail[1]:
                tail[1] -= 1


if __name__ == "__main__":
    instructions = []
    f = open("input.txt", "r")
    for line in f:
        s = line.strip()
        ins, num = line.split()
        n = int(num)
        instructions.append((ins, n))
    f.close()

    rope = Rope()
    for ins in instructions:
        rope.move(ins[0], ins[1])
    print("Part 1:", len(rope.been))
    rope = LongRope(10)
    for ins in instructions:
        rope.move(ins[0], ins[1])
    print("Part 2:", len(rope.been))

