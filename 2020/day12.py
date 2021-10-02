import math


data = []
f = open("day12.txt", "r")
for line in f:
    dat = line.strip()
    data.append((dat[0], int(dat[1:])))
f.close()

# print(data)


direction = 0
x = 0
y = 0
for inst in data:
    # print(x, y)
    act = inst[0]
    val = inst[1]
    if act == 'W':
        x -= val
    elif act == 'E':
        x += val
    elif act == 'S':
        y -= val
    elif act == 'N':
        y += val
    elif act == 'L':
        direction += val
    elif act == 'R':
        direction -= val
    elif act == 'F':
        angle = math.radians(direction)
        x += val * math.cos(angle)
        y += val * math.sin(angle)
    else:
        raise ValueError("'" + act + "' " + "is not a valid action")
# print(x, y)
print("Part 1:", int(abs(x) + abs(y)))


wx = 10
wy = 1
x = 0
y = 0
for inst in data:
    act = inst[0]
    val = inst[1]
    # print(act, val, x, y, wx, wy)
    if act == 'W':
        wx -= val
    elif act == 'E':
        wx += val
    elif act == 'S':
        wy -= val
    elif act == 'N':
        wy += val
    elif act == 'L' or act == 'R':
        mag = math.sqrt(wx**2 + wy**2)
        if wx == 0:
            if wy < 0:
                ang = 270
            elif wy > 0:
                ang = 90
            else:
                continue
        else:
            ref = abs(math.degrees(math.atan(wy/wx)))
            if wx >= 0:
                if wy >= 0:
                    ang = ref
                else:
                    ang = 360 - ref
            else:
                if wy >= 0:
                    ang = 180 - ref
                else:
                    ang = ref + 180
        if act == 'L':
            ang += val
        elif act == 'R':
            ang -= val
        ang = math.radians(ang)
        wx = round(mag * math.cos(ang))
        wy = round(mag * math.sin(ang))
    elif act == 'F':
        x += wx * val
        y += wy * val
    else:
        raise ValueError("'" + act + "' " + "is not a valid action")
# print(x, y)
print("Part 2:", round(abs(x) + abs(y)))


# Alternate solution for Part 2 (non-generalized)

# wx = 10
# wy = 1
# x = 0
# y = 0
# for inst in data:
#     act = inst[0]
#     val = inst[1]
#     # print(act, val, x, y, wx, wy)
#     if act == 'W':
#         wx -= val
#     elif act == 'E':
#         wx += val
#     elif act == 'S':
#         wy -= val
#     elif act == 'N':
#         wy += val
#     elif act == 'L':
#         if val == 180:
#             nwx = -wx
#             nwy = -wy
#         elif val == 90:
#             nwx = -wy
#             nwy = wx
#         elif val == 270:
#             nwx = wy
#             nwy = -wx
#         else:
#             raise ValueError
#         wx = nwx
#         wy = nwy
#     elif act == 'R':
#         if val == 180:
#             nwx = -wx
#             nwy = -wy
#         elif val == 90:
#             nwx = wy
#             nwy = -wx
#         elif val == 270:
#             nwx = -wy
#             nwy = wx
#         else:
#             raise ValueError
#         wx = nwx
#         wy = nwy
#     elif act == 'F':
#         x += wx * val
#         y += wy * val
#     else:
#         raise ValueError("'" + act + "' " + "is not a valid action")
# # print(x, y)
# print("Part 2:", int(abs(x) + abs(y)))

