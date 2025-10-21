t = input()
j = t[0]
d, s = 0, int(j)
for i in t[1: ]:
    if j != i:
        if d == 1: d, s = 0, s + 1
        else: d = 1
        j = i
    else: d = 1
print(s + (d and j == '1'))