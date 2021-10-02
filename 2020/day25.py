

data = []
f = open('day25.txt', 'r')
for line in f:
    data.append(int(line.strip()))

f.close()

size = 0
value = 1
snum = 7

i = 0
pub1 = None
pub2 = None
while True:
    if value == data[0]:
        pub1 = i
        if pub2 is not None:
            break
    if value == data[1]:
        pub2 = i
        if pub1 is not None:
            break
    value *= snum
    value = value % 20201227
    i += 1

# print(pub1, pub2)
value = 1
snum = data[1]
for i in range(pub1):
    value *= snum
    value = value % 20201227
print("Part 1:", value)
