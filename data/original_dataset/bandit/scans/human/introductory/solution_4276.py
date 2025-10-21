n, t = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
l = []
flag = False
for i in range(n):
    if a[i][1] <= t:
        l.append(a[i][0])
        flag = True
if flag:
    print(min(l))
else:
    print('TLE')