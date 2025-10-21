n, d = map(int, input().split())
line = list(map(int, input().split()))
pref = [0] * n
maxx = 0
for i in range(n):
    pref[i] = pref[max(i - 1, 0)] + line[i]
    maxx = max(maxx, pref[i])
maxr = [0] * n
for i in range(n - 1, -1, -1):
    if i == n - 1:
        maxr[i] = pref[i]
    else:
        maxr[i] = max(maxr[i + 1], pref[i])
sm = 0
bon = 0
ans = 0
b = True
if maxx > d:
    b = False
for i in range(n):
    elem = line[i]
    sm += elem
    if elem == 0:
        #print(sm, bon)
        if sm + bon < 0:
            ans += 1
            bon += max(0, d - (maxr[i] + bon))
        if sm + bon < 0:
            b = False
            break
    if sm + bon > d:
        b = False
        break
if b == False:
    print(-1)
else:
    print(ans)