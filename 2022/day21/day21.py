def multiply(left, right):
    return left * right


def add(left, right):
    return left + right


def subtract(left, right):
    return left - right


def divide(left, right):
    return left // right


symbols = {'*': multiply, '+': add, '-': subtract, '/': divide}
opposites = {'*': divide, '-': add, '+': subtract, '/': multiply}


class Node:
    nodes = {}

    def __init__(self, key, left, right, op):
        self.key = key
        self.value = None
        self.left = left
        self.right = right
        self.op = op
        Node.nodes[key] = self

    def get_value(self):
        if self.value is None:
            self.value = symbols[self.op](Node.nodes[self.left].get_value(), Node.nodes[self.right].get_value())
        return self.value

    def __repr__(self):
        if self.value is not None:
            return f"Node({self.key}: {self.value})"
        else:
            return f"Node({self.key}: {self.left} {self.op} {self.right})"


class Node2(Node):
    def get_value(self):
        if self.key == "humn":
            return None
        else:
            try:
                return super().get_value()
            except TypeError:
                return None


class Leaf(Node):
    def __init__(self, key, value):
        super().__init__(key, None, None, None)
        self.value = value


class Leaf2(Node2):
    def __init__(self, key, value):
        super().__init__(key, None, None, None)
        self.value = value


def get_input():
    with open("input.txt") as f:
        for line in f:
            key, value = line.split(": ")
            try:
                value = int(value)
                Leaf(key, value)
            except ValueError:
                left, op, right = value.split()
                Node(key, left, right, op)


def get_input2():
    with open("input.txt") as f:
        for line in f:
            key, value = line.split(": ")
            try:
                value = int(value)
                Leaf2(key, value)
            except ValueError:
                left, op, right = value.split()
                Node2(key, left, right, op)


def part1():
    get_input()
    print(f"Part 1: {Node.nodes['root'].get_value()}")
    Node.nodes.clear()


def part2():
    get_input2()
    root = Node.nodes['root']
    left = Node.nodes[root.left]
    right = Node.nodes[root.right]
    if left.get_value() is None:
        left.value = right.get_value()
        curr = left
    else:
        right.value = left.get_value()
        curr = right
    while True:
        if curr.key == "humn":
            break
        left = Node.nodes[curr.left]
        right = Node.nodes[curr.right]
        if left.get_value() is None:
            left.value = opposites[curr.op](curr.get_value(), right.get_value())
            curr = left
        else:
            if curr.op in ['-', '/']:
                right.value = symbols[curr.op](left.get_value(), curr.get_value())
            else:
                right.value = opposites[curr.op](curr.get_value(), left.get_value())
            curr = right
    print(f"Part 2: {curr.value}")


if __name__ == "__main__":
    part1()
    part2()
