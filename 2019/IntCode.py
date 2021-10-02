
def params(sequence, x, y, param1, param2):
    if param1 == 1:
        a = x
    else:
        a = sequence[x]
    if param2 == 1:
        b = y
    else:
        b = sequence[y]
    return a, b


def add(sequence, x, y, z, param1, param2):
    a, b = params(sequence, x, y, param1, param2)
    sequence[z] = a + b


def multiply(sequence, x, y, z, param1, param2):
    a, b = params(sequence, x, y, param1, param2)
    sequence[z] = a * b


def store(sequence, x, inputs):
    inp = inputs.pop(0)
    sequence[x] = int(inp)


def out(sequence, x, param1):
    if param1 == 0:
        return sequence[x]
    elif param1 == 1:
        return x


def jump_if_true(sequence, x, y, param1, param2):
    a, b = params(sequence, x, y, param1, param2)
    if a != 0:
        return b
    return None


def jump_if_false(sequence, x, y, param1, param2):
    a, b = params(sequence, x, y, param1, param2)
    if a == 0:
        return b
    return None


def less_than(sequence, x, y, z, param1, param2):
    a, b = params(sequence, x, y, param1, param2)
    if a < b:
        sequence[z] = 1
    else:
        sequence[z] = 0


def equals(sequence, x, y, z, param1, param2):
    a, b = params(sequence, x, y, param1, param2)
    if a == b:
        sequence[z] = 1
    else:
        sequence[z] = 0


def opcode(sequence, inputs):
    inst_point = 0
    while True:
        op = sequence[inst_point] % 100
        if op == 99:
            break
        parameters = str(sequence[inst_point]).rjust(5, '0')
        first_parameter = int(parameters[-3])
        second_parameter = int(parameters[-4])
        pos1 = sequence[inst_point + 1]
        pos2 = sequence[inst_point + 2]
        pos3 = sequence[inst_point + 3]
        if op == 1:
            add(sequence, pos1, pos2, pos3, first_parameter, second_parameter)
            inst_point += 4
        elif op == 2:
            multiply(sequence, pos1, pos2, pos3, first_parameter, second_parameter)
            inst_point += 4
        elif op == 3:
            store(sequence, pos1, inputs)
            inst_point += 2
        elif op == 4:
            output = out(sequence, pos1, first_parameter)
            inst_point += 2
            return output
        elif op == 5:
            chg = jump_if_true(sequence, pos1, pos2, first_parameter, second_parameter)
            if chg is None:
                inst_point += 3
            else:
                inst_point = chg
        elif op == 6:
            chg = jump_if_false(sequence, pos1, pos2, first_parameter, second_parameter)
            if chg is None:
                inst_point += 3
            else:
                inst_point = chg
        elif op == 7:
            less_than(sequence, pos1, pos2, pos3, first_parameter, second_parameter)
            inst_point += 4
        elif op == 8:
            equals(sequence, pos1, pos2, pos3, first_parameter, second_parameter)
            inst_point += 4
