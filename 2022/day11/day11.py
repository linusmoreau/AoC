from collections import deque


class Monkey:
    monkeys = []

    def __init__(self, items: deque, operation, divisor, target, alt_target):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.target = target
        self.alt_target = alt_target
        self.inspections = 0
        self.monkeys.append(self)

    def inspect_item(self):
        item = self.items.popleft()
        worry = self.operation(item) // 3
        if worry % self.divisor == 0:
            self.monkeys[self.target].catch(worry)
        else:
            self.monkeys[self.alt_target].catch(worry)
        self.inspections += 1

    def catch(self, item):
        self.items.append(item)

    def has_item(self):
        return len(self.items) > 0


class RemainderMonkey:
    monkeys = []

    def __init__(self, items: deque, operation, divisor, target, alt_target):
        self.items = items
        self.operation = operation
        self.divisor = divisor
        self.target = target
        self.alt_target = alt_target
        self.inspections = 0
        self.remainders = deque()
        self.monkeys.append(self)

    def inspect_item(self):
        remainder = self.remainders.popleft()
        worry = self.operation(remainder.make_number())
        remainder = Remainders([worry % m.divisor for m in self.monkeys])

        if worry % self.divisor == 0:
            self.monkeys[self.target].catch(remainder)
        else:
            self.monkeys[self.alt_target].catch(remainder)
        self.inspections += 1

    def catch(self, remainder):
        self.remainders.append(remainder)

    def has_item(self):
        return len(self.remainders) > 0

    def set_up_remainders(self):
        for item in self.items:
            self.remainders.append(Remainders([item % m.divisor for m in self.monkeys]))


class Remainders:
    divisors = []
    cache = {}

    def __init__(self, remainders):
        self.remainders = remainders
        self.max_divisor = 0
        self.max_divisor_i = 0
        for i, divisor in enumerate(self.divisors):
            if divisor > self.max_divisor:
                self.max_divisor = divisor
                self.max_divisor_i = i

    def make_number(self):
        try:
            n = self.cache[tuple(self.remainders)]
        except KeyError:
            n = self.remainders[self.max_divisor_i]
            while True:
                for i in range(len(self.divisors)):
                    if n % self.divisors[i] != self.remainders[i]:
                        n += self.max_divisor
                        break
                else:
                    break
            self.cache[tuple(self.remainders)] = n
        return n


def make_op(op, num):
    if num == "old":
        if op == "*":
            return lambda old: old * old
        elif op == "+":
            return lambda old: old + old
        else:
            raise Exception("Invalid operator")
    else:
        if op == "*":
            return lambda old: old * num
        elif op == "+":
            return lambda old: old + num
        else:
            raise Exception("Invalid operator")


def make_monkey(lines):
    items_line = lines[1]
    items = deque(map(int, items_line[items_line.find(":") + 2:].strip().split(", ")))
    op_line = lines[2].split()
    op = op_line[-2]
    num = op_line[-1]
    if num != "old":
        num = int(num)
    operation = make_op(op, num)
    divisor = int(lines[3].split()[-1])
    true_target = int(lines[4].split()[-1])
    false_target = int(lines[5].split()[-1])
    Monkey(items, operation, divisor, true_target, false_target)
    RemainderMonkey(items.copy(), operation, divisor, true_target, false_target)


def play_round():
    for monkey in Monkey.monkeys:
        while monkey.has_item():
            monkey.inspect_item()


def play_round_but_stress():
    for monkey in RemainderMonkey.monkeys:
        while monkey.has_item():
            monkey.inspect_item()


def read_file():
    f = open("input.txt", "r")
    monkey_lines = []
    for line in f:
        s = line.strip()
        if len(line) == 1:
            continue
        monkey_lines.append(s)
        if len(monkey_lines) == 6:
            make_monkey(monkey_lines)
            monkey_lines = []
    f.close()


if __name__ == "__main__":
    read_file()
    for _ in range(20):
        play_round()
    results = sorted([monkey.inspections for monkey in Monkey.monkeys])
    print("Part 1:", results[-1] * results[-2])

    for m in RemainderMonkey.monkeys:
        Remainders.divisors.append(m.divisor)
    for m in RemainderMonkey.monkeys:
        m.set_up_remainders()

    for i in range(10000):
        # if i % 10 == 0:
        #     print(i, [monkey.inspections for monkey in RemainderMonkey.monkeys])
        play_round_but_stress()
    results = sorted([monkey.inspections for monkey in RemainderMonkey.monkeys])
    print("Part 2:", results[-1] * results[-2])

