

data = []
f = open("day4.txt", "r")

entry = {}
for line in f:
    if len(line) == 1:
        data.append(entry)
        entry = {}
    else:
        for field in line.split():
            temp = field.split(':')
            entry[temp[0]] = temp[1]
data.append(entry)

f.close()

# print(data)

necessary = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
num = 0
for entry in data:
    works = True
    for field in necessary:
        try:
            val = entry[field]
            if field == "byr":
                if len(val) != 4 or int(val) < 1920 or int(val) > 2002:
                    works = False
            elif field == "iyr":
                if len(val) != 4 or int(val) < 2010 or int(val) > 2020:
                    works = False
            elif field == "eyr":
                if len(val) != 4 or int(val) < 2020 or int(val) > 2030:
                    works = False
            elif field == "hgt":
                try:
                    hgt = int(val[:-2])
                    if val[-2:] == "cm":
                        if hgt < 150 or hgt > 193:
                            works = False
                    elif val[-2:] == "in":
                        if hgt < 59 or hgt > 76:
                            works = False
                    else:
                        works = False
                except ValueError:
                    works = False
            elif field == "hcl":
                if val[0] != "#":
                    works = False
                valid = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}
                for i in range(1, 7):
                    try:
                        if val[i] not in valid:
                            works = False
                    except IndexError:
                        works = False
            elif field == "ecl":
                valid = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
                if val not in valid:
                    works = False
            elif field == "pid":
                try:
                    pid = int(val)
                except ValueError:
                    works = False
                if len(val) != 9:
                    works = False
        except KeyError:
            works = False
    if works:
        num += 1

print(num)
