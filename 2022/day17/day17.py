
class Grid:
    def __init__(self, width, spawn):
        self.width = width
        self.spawn = spawn
        self.grid = []

    def new_rock(self, shape):
        p = (self.spawn[0], self.height() + self.spawn[1])
        return shape(p)

    def conflict(self, p) -> bool:
        return p[1] < 0 or p[0] < 0 or p[0] >= self.width or (p[1] < len(self.grid) and self.grid[p[1]][p[0]])

    def place(self, p):
        while len(self.grid) <= p[1]:
            self.generate_row()
        self.grid[p[1]][p[0]] = True

    def generate_row(self):
        self.grid.append([False for _ in range(self.width)])

    def height(self):
        return len(self.grid)

    def get_surface(self):
        surface = [-1 for _ in range(self.width)]
        i = 0
        countdown = None
        while countdown is None or countdown > 0:
            for a in range(self.width):
                if surface[a] == -1:
                    if self.conflict((a, self.height() - 1 - i)):
                        surface[a] = i
            if countdown is None and -1 not in surface[1:-1]:
                countdown = 1000
            elif countdown is not None:
                countdown -= 1
            i += 1
            # print(countdown, surface)

        return surface


class Rock:
    def __init__(self, pos):
        self.pos = pos

    def drop(self, grid):
        pos = (self.pos[0], self.pos[1] - 1)
        return self.move(grid, pos)

    def push(self, grid, dif):
        pos = (self.pos[0] + dif, self.pos[1])
        return self.move(grid, pos)

    def move(self, grid, pos):
        if self.conflict(grid, pos):
            return False
        else:
            self.pos = pos
            return True

    def conflict(self, grid, pos) -> bool:
        raise Exception("Child class lacks implementation of conflict(self, grid, pos)")

    def place(self, grid):
        raise Exception("Child class lacks implementation of place(self, grid)")


class HorizontalLine(Rock):
    def conflict(self, grid: Grid, pos) -> bool:
        for i in range(4):
            if grid.conflict((pos[0] + i, pos[1])):
                return True
        return False

    def place(self, grid: Grid):
        for i in range(4):
            grid.place((self.pos[0] + i, self.pos[1]))


class Plus(Rock):
    def conflict(self, grid: Grid, pos) -> bool:
        points = [(pos[0], pos[1] + 1), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), (pos[0] + 1, pos[1] + 2),
                  (pos[0] + 2, pos[1] + 1)]
        for p in points:
            if grid.conflict(p):
                return True
        return False

    def place(self, grid: Grid):
        points = [(self.pos[0], self.pos[1] + 1), (self.pos[0] + 1, self.pos[1]), (self.pos[0] + 1, self.pos[1] + 1),
                  (self.pos[0] + 1, self.pos[1] + 2), (self.pos[0] + 2, self.pos[1] + 1)]
        for p in points:
            grid.place(p)


class BackwardsL(Rock):
    def conflict(self, grid: Grid, pos) -> bool:
        points = [(pos[0], pos[1]), (pos[0] + 1, pos[1]), (pos[0] + 2, pos[1]), (pos[0] + 2, pos[1] + 1),
                  (pos[0] + 2, pos[1] + 2)]
        for p in points:
            if grid.conflict(p):
                return True
        return False

    def place(self, grid: Grid):
        points = [(self.pos[0], self.pos[1]), (self.pos[0] + 1, self.pos[1]), (self.pos[0] + 2, self.pos[1]),
                  (self.pos[0] + 2, self.pos[1] + 1), (self.pos[0] + 2, self.pos[1] + 2)]
        for p in points:
            grid.place(p)


class VerticalLine(Rock):
    def conflict(self, grid: Grid, pos) -> bool:
        for i in range(4):
            if grid.conflict((pos[0], pos[1] + i)):
                return True
        return False

    def place(self, grid: Grid):
        for i in range(4):
            grid.place((self.pos[0], self.pos[1] + i))


class Square(Rock):
    def conflict(self, grid: Grid, pos) -> bool:
        points = [(pos[0], pos[1]), (pos[0] + 1, pos[1]), (pos[0] + 1, pos[1] + 1), (pos[0], pos[1] + 1)]
        for p in points:
            if grid.conflict(p):
                return True
        return False

    def place(self, grid: Grid):
        points = [(self.pos[0], self.pos[1]), (self.pos[0] + 1, self.pos[1]), (self.pos[0] + 1, self.pos[1] + 1),
                  (self.pos[0], self.pos[1] + 1)]
        for p in points:
            grid.place(p)


def part1():
    grid = Grid(7, (2, 3))
    n = 0
    for i in range(2022):
        rock = grid.new_rock(shapes[i % len(shapes)])

        while True:
            jet = jets[n % len(jets)]
            if jet == "<":
                rock.push(grid, -1)
            elif jet == ">":
                rock.push(grid, 1)
            else:
                raise Exception("Unexpected jet")
            n += 1

            if not rock.drop(grid):
                rock.place(grid)
                break
    print("Part 1:", grid.height())


def part2():
    cache = {}
    tot_rocks = 1000000000000
    grid = Grid(7, (2, 3))
    i = 0
    n = 0
    rocks_placed = 0
    fill = 0
    done = False
    while rocks_placed < tot_rocks:
        if i >= len(shapes):
            i %= len(shapes)
        rock = grid.new_rock(shapes[i])

        while True:
            if n >= len(jets):
                n %= len(jets)
                if not done:
                    key = (i, n, tuple(grid.get_surface()))
                    try:
                        prev_placed, height = cache[key]
                        repeatedly_placed = rocks_placed - prev_placed
                        repeat = (tot_rocks - rocks_placed) // repeatedly_placed
                        newly_placed = repeat * (rocks_placed - prev_placed)
                        fill = (grid.height() - height) * repeat
                        rocks_placed += newly_placed
                        done = True
                        continue
                    except KeyError:
                        cache[key] = (rocks_placed, grid.height())
            jet = jets[n]
            if jet == "<":
                rock.push(grid, -1)
            elif jet == ">":
                rock.push(grid, 1)
            else:
                raise Exception("Unexpected jet")
            n += 1

            if not rock.drop(grid):
                rock.place(grid)
                i += 1
                rocks_placed += 1
                break
    print("Part 2:", grid.height() + fill)


def read_file():
    f = open("input.txt", "r")
    jets = ""
    for line in f:
        jets = line.strip()
    f.close()
    return jets


if __name__ == "__main__":
    jets = read_file()
    shapes = [HorizontalLine, Plus, BackwardsL, VerticalLine, Square]

    part1()
    part2()





