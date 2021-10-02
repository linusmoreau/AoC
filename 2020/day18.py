
expressions = []
f = open("day18.txt", "r")
for line in f:
    expressions.append(line)


# Part 1


def evaluate(e):
    if len(e) == 1:
        return e[0]
    else:
        n = 0
        if e[1] == '+':
            n = int(e[0]) + int(e[2])
        elif e[1] == '*':
            n = int(e[0]) * int(e[2])
        return evaluate([n] + e[3:])


def process(e):
    ne = ''
    start = 0
    for i, c in enumerate(e):
        if c == '(':
            ne = ''
            start = i
        elif c == ')':
            return process(e[:start] + str(evaluate(ne.split())) + e[i + 1:])
        else:
            ne += c
    return evaluate(e.split())


total = 0
for e in expressions:
    total += process(e)

print("For part 1:", total)


# Part 2:

def evaluate2(e):
    if len(e) == 1:
        return e[0]
    elif '+' in e:
        i = e.index('+')
        return evaluate2(e[:i - 1] + [int(e[i - 1]) + int(e[i + 1])] + e[i + 2:])
    else:
        n = 0
        if e[1] == '+':
            n = int(e[0]) + int(e[2])
        elif e[1] == '*':
            n = int(e[0]) * int(e[2])
        return evaluate2([n] + e[3:])


def process2(e):
    ne = ''
    start = 0
    for i, c in enumerate(e):
        if c == '(':
            ne = ''
            start = i
        elif c == ')':
            return process2(e[:start] + str(evaluate2(ne.split())) + e[i + 1:])
        else:
            ne += c
    return evaluate2(e.split())


total = 0
for e in expressions:
    total += process2(e)

print("For part 2:", total)
