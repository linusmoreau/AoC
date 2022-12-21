

def read_commands(instructions):
    cycle = 1
    x = 1
    log = [None, 1]
    for ins in instructions:
        s = ins.split()
        cmd = s[0]
        if cmd == "noop":
            cycle += 1
            log.append(x)
        elif cmd == "addx":
            cycle += 2
            log.append(x)
            x += int(s[1])
            log.append(x)
        else:
            raise Exception
    return log


def interpret_log(log):
    total = 0
    for i in range(6):
        n = 20 + i * 40
        total += log[n] * n
    return total


def render_crt(log, w, h):
    for y in range(h):
        for x in range(w):
            cycle = x + y * w + 1
            sprite = range(log[cycle] - 1, log[cycle] + 2)
            if x in sprite:
                print("#", end="")
            else:
                print(".", end="")
        print()


if __name__ == "__main__":
    instructions = []
    f = open("input.txt", "r")
    for line in f:
        s = line.strip()
        instructions.append(s)
    f.close()

    log = read_commands(instructions)
    print("Part 1:", interpret_log(log))
    print("Part 2:")
    render_crt(log, 40, 6)

