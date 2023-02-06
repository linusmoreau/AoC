
class Node:
    count = 0

    def __init__(self, num, forward, backward):
        self.forward = forward
        self.backward = backward
        self.num = num

    def move(self):
        if self.num != 0:
            self.backward.forward = self.forward
            self.forward.backward = self.backward
            forward = self.forward
            if self.num > 0:
                for _ in range(self.num % (Node.count - 1)):
                    forward = forward.forward
            elif self.num < 0:
                for _ in range(abs(self.num) % (Node.count - 1)):
                    forward = forward.backward
            else:
                return
            self.forward = forward
            self.backward = forward.backward
            self.forward.backward = self
            self.backward.forward = self

    def __repr__(self):
        return f"Node({self.num})"


def part1(nums):
    zero = -1
    for num in nums:
        num.move()
        if num.num == 0:
            zero = num
    total = 0
    curr = zero
    for _ in range(3):
        for a in range(1000):
            curr = curr.forward
        total += curr.num
    print(f"Part 1: {total}")


def part2(nums):
    zero = -1
    for num in nums:
        num.num *= 811589153
        if num.num == 0:
            zero = num
    for _ in range(10):
        for num in nums:
            num.move()
    total = 0
    curr = zero
    for _ in range(3):
        for a in range(1000):
            curr = curr.forward
        total += curr.num
    print(f"Part 2: {total}")


def get_input():
    Node.count = 0
    nums = []
    with open("input.txt") as f:
        lines = f.readlines()
    for line in lines:
        num = int(line.strip())
        if len(nums) == 0:
            node = Node(num, None, None)
        elif len(nums) == len(lines) - 1:
            node = Node(num, nums[0], nums[-1])
            node.backward.forward = node
            node.forward.backward = node
        else:
            node = Node(num, None, nums[-1])
            node.backward.forward = node
        Node.count += 1
        nums.append(node)
    return nums


if __name__ == "__main__":
    part1(get_input())
    part2(get_input())
