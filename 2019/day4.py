
x = 246540
y = 787420
counter = 0
for i in range(x, y):
    adj = False
    works = True
    s = str(i) + "0"
    for j in range(len(s)-2):
        if s[j] == s[j+1] and s[j] != s[j+2]:
            if j != 0:
                if s[j-1] != s[j]:
                    adj = True
                    break
            else:
                adj = True
                break
    for j in range(0, len(s)-2):
        if s[j] > s[j+1]:
            works = False
            break
    else:
        if works and adj:
            counter += 1
print(counter)
