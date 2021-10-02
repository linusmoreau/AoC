
def fuel_required(mass):
    fuel = mass // 3 - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + fuel_required(fuel)


total = 0
f = open("day1_input.txt", "r")
for line in f:
    total += fuel_required(int(line))
print(total)
f.close()
