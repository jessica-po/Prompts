l = []

for c in input():
    if len(l) > 0 and l[-1] == c:
        l.pop()
    else:
        l.append(c)

print('Yes' if len(l) == 0 else 'No')