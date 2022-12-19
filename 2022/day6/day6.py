
def find_first_packet(signal):
    for i, c in enumerate(signal):
        if i > 2:
            r = signal[i - 3:i + 1]
            for a in r:
                if r.count(a) != 1:
                    break
            else:
                return i + 1, r


def find_first_message(signal):
    for i, c in enumerate(signal):
        if i > 12:
            r = signal[i - 13:i + 1]
            for a in r:
                if r.count(a) != 1:
                    break
            else:
                return i + 1, r


if __name__ == "__main__":
    signal = ""
    f = open("input.txt", "r")
    is_instruction = False
    for line in f:
        signal += line.strip()
    f.close()
    print("Part 1:", find_first_packet(signal)[0])
    print("Part 2:", find_first_message(signal)[0])

