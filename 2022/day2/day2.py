

win = 6
draw = 3
lose = 0

x = 1
y = 2
z = 3

rock = 0
paper = 1
scissors = 2

points = [x, y, z]


def move(symbol):
    if symbol in "AX":
        return rock, x
    elif symbol in "BY":
        return paper, y
    elif symbol in "CZ":
        return scissors, z


def outcome_points(opp, you):
    if (opp + 1) % 3 == you % 3:
        return win
    elif opp % 3 == (you + 1) % 3:
        return lose
    else:
        return draw


def choose_move(opp, sym):
    if sym == "X":
        move = opp - 1
    elif sym == "Y":
        move = opp
    else:
        move = opp + 1
    if move < 0:
        move += 3
    elif move > 2:
        move -= 3
    return move


def outcome_points2(outcome):
    if outcome == "X":
        return lose
    elif outcome == "Y":
        return draw
    elif outcome == "Z":
        return win


if __name__ == "__main__":
    rounds = []
    f = open("input.txt", "r")
    for line in f:
        s = line.strip()
        opp, you = s.split()
        rounds.append((opp, you))
    f.close()

    total = 0
    for r in rounds:
        you, p = move(r[1])
        opp, _ = move(r[0])
        op = outcome_points(opp, you)
        total += p + op
    print("Part 1:", total)

    total = 0
    for r in rounds:
        opp, _ = move(r[0])
        m = choose_move(opp, r[1])
        total += points[m] + outcome_points2(r[1])
    print("Part 2:", total)

