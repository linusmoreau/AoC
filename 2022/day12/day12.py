
from collections import deque


def read_file():
    f = open("input.txt", "r")
    grid = []
    i = 0
    start = None
    end = None
    for line in f:
        s = line.strip()
        grid.append(s)
        a = s.find("S")
        if a != -1:
            start = (a, i)
        b = s.find("E")
        if b != -1:
            end = (b, i)
        i += 1
    f.close()
    dim = (len(grid[0]), len(grid))
    return grid, start, end, dim


def adjacent(p, dim):
    a = []
    if p[0] > 0:
        a.append((p[0] - 1, p[1]))
    if p[1] > 0:
        a.append((p[0], p[1] - 1))
    if p[0] < dim[0] - 1:
        a.append((p[0] + 1, p[1]))
    if p[1] < dim[1] - 1:
        a.append((p[0], p[1] + 1))
    return a


def climbable(p, t, grid):
    a = grid[p[1]][p[0]]
    b = grid[t[1]][t[0]]
    if b == "E":
        return a == "z"
    elif a == "S":
        return b == "a"
    else:
        return ord(a) >= ord(b) - 1


if __name__ == "__main__":
    grid, start, end, dim = read_file()
    reached = set()
    reached.add(start)
    todo = deque()
    todo.append((start, [start]))
    while len(todo) > 0:
        p, steps = todo.popleft()
        for n in adjacent(p, dim):
            if n not in reached and climbable(p, n, grid):
                if grid[n[1]][n[0]] == "E":
                    fullpath = steps + [n]
                    print("Part 1:", len(steps))
                    todo.clear()
                    break
                todo.append((n, steps + [n]))
                reached.add(n)

    reached = set()
    reached.add(end)
    todo = deque()
    todo.append((end, [end]))
    while len(todo) > 0:
        p, steps = todo.popleft()
        for n in adjacent(p, dim):
            if n not in reached and climbable(n, p, grid):
                if grid[n[1]][n[0]] == "a":
                    fullpath = steps + [n]
                    print("Part 2:", len(steps))
                    todo.clear()
                    break
                todo.append((n, steps + [n]))
                reached.add(n)


