n = int(input())
a = input().strip()
nextl = [-1] * n
lastr = [-1] * n
ll = -1
for i in range(n):
    if a[i] == "R":
        ll = i
    if a[i] == "L":
        ll = -1
    lastr[i] = ll
nl = -1
for i in range(n - 1, -1, -1):
    if a[i] == "L":
        nl = i
    if a[i] == "R":
        nl = -1
    nextl[i] = nl
ans = 0
#print(lastr)
#print(nextl)
for i in range(n):
    if nextl[i] == lastr[i] == -1:
        ans += 1
    if nextl[i] == -1 or lastr[i] == -1:
        continue
    d1 = nextl[i] - i
    d2 = i - lastr[i]
    if d1 == d2:
        ans += 1
print(ans)