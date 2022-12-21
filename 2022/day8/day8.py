
class Tree:
    def __init__(self, pos, height):
        self.pos = pos
        self.height = height

    def look(self, trees, view):
        i = 1
        while True:
            try:
                if view == "west":
                    tree = trees[(self.pos[0] - i, self.pos[1])]
                elif view == "east":
                    tree = trees[(self.pos[0] + i, self.pos[1])]
                elif view == "north":
                    tree = trees[(self.pos[0], self.pos[1] - i)]
                else:
                    tree = trees[(self.pos[0], self.pos[1] + i)]
                if tree.height >= self.height:
                    break
            except KeyError:
                i -= 1
                break
            i += 1
        return i

    def get_scenic_score(self, trees):
        return self.look(trees, "west") * self.look(trees, "east") * \
               self.look(trees, "north") * self.look(trees, "south")


def get_visible_from_west(trees, w, h):
    visible = set()
    for i in range(h):
        tallest = -1
        for j in range(w - 1, -1, -1):
            tree = trees[(j, i)]
            if tree.height > tallest:
                visible.add(tree)
                tallest = tree.height
    return visible


def get_visible_from_east(trees, w, h):
    visible = set()
    for i in range(h):
        tallest = -1
        for j in range(w):
            tree = trees[(j, i)]
            if tree.height > tallest:
                visible.add(tree)
                tallest = tree.height
    return visible


def get_visible_from_north(trees, w, h):
    visible = set()
    for i in range(w):
        tallest = -1
        for j in range(h):
            tree = trees[(i, j)]
            if tree.height > tallest:
                visible.add(tree)
                tallest = tree.height
    return visible


def get_visible_from_south(trees, w, h):
    visible = set()
    for i in range(w):
        tallest = -1
        for j in range(h - 1, -1, -1):
            tree = trees[(i, j)]
            if tree.height > tallest:
                visible.add(tree)
                tallest = tree.height
    return visible


def get_visible(trees, w, h):
    visible = get_visible_from_west(trees, w, h)
    visible = visible.union(get_visible_from_east(trees, w, h))
    visible = visible.union(get_visible_from_north(trees, w, h))
    visible = visible.union(get_visible_from_south(trees, w, h))
    return visible


def get_highest_scenic_score(trees):
    highest = 0
    for tree in trees.values():
        s = tree.get_scenic_score(trees)
        if s > highest:
            highest = s
    return highest


if __name__ == "__main__":
    trees = {}
    f = open("input.txt", "r")
    i = 0
    w = None
    for line in f:
        s = line.strip()
        if w is None:
            w = len(s)
        for j in range(len(s)):
            pos = (j, i)
            trees[pos] = Tree(pos, int(s[j]))
        i += 1
    h = i
    f.close()

    visible = get_visible(trees, w, h)
    print("Part 1:", len(visible))
    print("Part 2:", get_highest_scenic_score(trees))

