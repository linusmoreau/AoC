
def add(numbers, x, y, z):
    numbers[z] = numbers[x] + numbers[y]


def multiply(numbers, x, y, z):
    numbers[z] = numbers[x] * numbers[y]


def opcode(sequence):
    inst_point = 0
    while True:
        op = sequence[inst_point]
        if op == 99:
            break
        pos1 = sequence[inst_point + 1]
        pos2 = sequence[inst_point + 2]
        pos3 = sequence[inst_point + 3]
        if op == 1:
            add(sequence, pos1, pos2, pos3)
        elif op == 2:
            multiply(sequence, pos1, pos2, pos3)
        inst_point += 4
    return sequence[0]


inputs = ""
f = open("day2_input.txt", "r")
for line in f:
    inputs += line
f.close()
inputs = inputs.split(',')
numbers = []
for i in inputs:
    numbers.append(int(i))

for noun in range(100):
    for verb in range(100):
        check = numbers.copy()
        check[1] = noun
        check[2] = verb
        if opcode(check) == 19690720:
            print(100 * noun + verb)
            break
