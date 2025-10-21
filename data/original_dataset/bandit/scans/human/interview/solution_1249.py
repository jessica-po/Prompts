n, k, m, s = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
need = len(c)
rez = n - m * k
kek = [0 for i in range(500007)]
cur_kek = [0 for i in range(500007)]
for i in c:
    kek[i] += 1
r = 0
if (rez == 0):
    lol = need
    for i in range(0, n, k):
        for j in range(i, i + k):
            if kek[a[j]] > cur_kek[a[j]]:
                need -= 1
            cur_kek[a[j]] += 1
        if (need == 0):
            print(0)
            break
        for j in range(i, i + k):
            cur_kek[a[j]] = 0
    else:
        print(-1)
    return
meshayut = 0 if kek[a[0]] else 1
if kek[a[0]]:
    need -= 1
cur_kek[a[0]] += 1
ans = []
for l in range(n):
    while need > 0 and r < n - 1:
        r += 1
        if (kek[a[r]] > cur_kek[a[r]]):
            need -= 1
            cur_kek[a[r]] += 1
        else:
            cur_kek[a[r]] += 1
            meshayut += 1
        #print(r, need)
    need_to_cut = l % k
    cur = r - l + 1
    razn = cur - k
    #print(l, r, need_to_cut, razn, meshayut, cur, need)
    #print(need, razn + need_to_cut, rez, meshayut + not_useful, razn + need_to_cut)
    if (need == 0 and razn + need_to_cut <= rez and meshayut >= razn):
        rezhem = razn
        for j in range(l - need_to_cut, l):
            ans.append(j + 1)
        for j in range(l, r + 1):
            if kek[a[j]]:
                kek[a[j]] -= 1
            elif rezhem:
                ans.append(j + 1)
                rezhem -= 1
        print(len(ans))
        print(' '.join(map(str, ans)))
        break
    if (kek[a[l]]):
        if cur_kek[a[l]] > kek[a[l]]:
            meshayut -= 1
        else:
            need += 1
    else:
        meshayut -= 1
    cur_kek[a[l]] -= 1
else:
    print(-1)