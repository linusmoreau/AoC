class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.dirs = {}
        self.files = {}
        self.size = 0

    def add_dir(self, name, d):
        self.dirs[name] = d
        self.add_child(name, d)
        self.add_size(d.size)

    def add_file(self, name, file):
        self.files[name] = file
        self.add_child(name, file)
        self.add_size(file.size)

    def add_child(self, name, child):
        self.children[name] = child

    def get_child(self, name):
        return self.children[name]

    def add_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size)


class File:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent


def parse_commands(lines):
    top_dir = Directory("/", None)
    current: (Directory, None) = None
    for line in lines:
        if line[0] == "$":
            ins = line.split()
            command = ins[1]
            if command == "cd":
                name = ins[2]
                if name == "..":
                    current = current.parent
                elif name == "/":
                    current = top_dir
                else:
                    current = current.get_child(name)
            elif command == "ls":
                pass
        else:
            inf = line.split()
            name = inf[1]
            if inf[0] == "dir":
                current.add_dir(name, Directory(name, current))
            else:
                current.add_file(name, File(name, int(inf[0]), current))
    return top_dir


def get_dirs_under_size(c: Directory, size: int):
    dirs = []
    if c.size <= size:
        dirs.append(c)
    for d in c.dirs.values():
        dirs.extend(get_dirs_under_size(d, size))
    return dirs


def get_dirs_over_size(c: Directory, size: int):
    dirs = []
    if c.size >= size:
        dirs.append(c)
    for d in c.dirs.values():
        dirs.extend(get_dirs_over_size(d, size))
    return dirs


if __name__ == "__main__":
    command_lines = []
    f = open("input.txt", "r")
    is_instruction = False
    for line in f:
        command_lines.append(line.strip())
    f.close()

    home = parse_commands(command_lines)
    print("Part 1:", sum([d.size for d in get_dirs_under_size(home, 100000)]))
    print("Part 2:", min([d.size for d in get_dirs_over_size(home, 30000000 - (70000000 - home.size))]))

