from sys import stdin

n = int(input())
a = [int(x) for x in input().split()]

f = False
for i in range(len(a)):
    if a[i] != 0:
        ln = i
        f = True
        break
if not f:
    print('NO')
else:
    print('YES')
    l = 0
    i = ln + 1
    ans = []
    while i < len(a):
        if a[i] == 0:
            i += 1
        else:
            ans.append((l+1, i))
            l = i
            i += 1
    if l < len(a):
        ans.append((l+1, i))
    print(len(ans))
    for i in ans:
        print(i[0],i[1])