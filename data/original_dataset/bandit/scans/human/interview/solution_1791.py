t = {}
for i, c in enumerate(input()):
    if c not in t: t[c] = (i, 1)
    elif (t[c][0] - i) & 1: t[c] = (i, t[c][1] + 1)
print(max(b for a, b in t.values()))