n = int(input())

line = input().split()
lst = []
for num in line:
    lst.append(int(num))

cnt1 = [0]
cnt2 = [0]
c1 = 0
c2 = 0

for num in lst:
    if num == 1:
        c1 += 1
        cnt1.append(c2)
    else:
        c2 += 1
        cnt2.append(c1)

w = lst[n - 1]
ans = []
c1 = len(cnt1)
c2 = len(cnt2)
for t in range(n, 0, -1):
    s1 = 0
    s2 = 0
    i1 = 0
    i2 = 0
    l = 1
    while i1 < c1 and i2 < c2:
        if i1 + t >= c1 and i2 + t >= c2:
            if l == 1 and l == w and i1 + 1 == c1 and s1 > s2:
                ans.append((s1, t))
            elif l == 2 and l == w and i2 + 1 == c2 and s2 > s1:
                ans.append((s2, t))
            break
        elif i2 + t >= c2:
            s1 += 1
            l = 1
            i1 += t
            i2 = cnt1[i1]
        elif i1 + t >= c1:
            s2 += 1
            l = 2
            i2 += t
            i1 = cnt2[i2]
        else:
            if cnt1[i1 + t] < i2 + t:
                s1 += 1
                l = 1
                i1 += t
                i2 = cnt1[i1]
            else:
                s2 += 1
                l = 2
                i2 += t
                i1 = cnt2[i2]

ans.sort()

print(int(len(ans)))
for line in ans:
    print(str(line[0]) + ' ' + str(line[1]))