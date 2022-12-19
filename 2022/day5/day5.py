from typing import *
from collections import deque


class Crate:
    def __init__(self, mark: str):
        self.mark = mark


class Stacks:
    def __init__(self, num):
        self.num = num
        self.stacks: List[deque[Crate]] = [deque() for _ in range(self.num + 1)]

    def insert(self, c, stack):
        self.stacks[stack].appendleft(c)

    def extend(self, d, stack):
        self.stacks[stack].extendleft(d)

    def pop(self, stack):
        return self.stacks[stack].popleft()

    def peek(self, stack):
        if len(self.stacks[stack]) == 0:
            return " "
        return self.stacks[stack][0].mark

    def tops(self):
        s = ""
        for i in range(1, len(self.stacks)):
            s += stacks.peek(i)
        return s


class Instruction:
    def __init__(self, amount, orig, dest):
        self.amount = amount
        self.orig = orig
        self.dest = dest

    def apply(self, stacks):
        for i in range(self.amount):
            crate = stacks.pop(self.orig)
            stacks.insert(crate, self.dest)

    def apply9001(self, stacks):
        d: deque[Crate] = deque()
        for i in range(self.amount):
            crate = stacks.pop(self.orig)
            d.appendleft(crate)
        stacks.extend(d, self.dest)


def process_stack_lines(stack_lines):
    num = int(stack_lines[-1].strip().split()[-1])
    stacks = Stacks(num)
    for i in range(len(stack_lines) - 2, -1, -1):
        line = stack_lines[i]
        for j in range(num):
            k = j * 4 + 1
            if k >= len(line):
                break
            if line[k] != " ":
                stacks.insert(Crate(line[k]), j + 1)
    return stacks


if __name__ == "__main__":
    stack_lines = []
    instructions = []
    f = open("input.txt", "r")
    is_instruction = False
    for line in f:
        s = line.strip("\n")
        if s == "":
            is_instruction = True
        elif is_instruction:
            parts = s.split()
            # print(int(parts[1]), int(parts[3]), int(parts[5]))
            instructions.append(Instruction(int(parts[1]), int(parts[3]), int(parts[5])))
        else:
            stack_lines.append(s)
    f.close()

    stacks = process_stack_lines(stack_lines)
    for instruction in instructions:
        instruction.apply(stacks)
    print("Part 1:", stacks.tops())

    stacks = process_stack_lines(stack_lines)
    for instruction in instructions:
        instruction.apply9001(stacks)
    print("Part 2:", stacks.tops())

