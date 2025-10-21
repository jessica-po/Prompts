n = int(input())
r = {}
ans = 0
for i in input():
    if i == i.lower():
        if i in r:
            r[i] += 1
        else:
            r[i] = 1
    else:
        i = i.lower()
        if i in r and r[i] > 0:
            r[i] -= 1
        else:
            ans += 1
print(ans)