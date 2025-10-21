import sys
n, m = list(map(int, sys.stdin.readline().split()))
vis = [0] * 1000005
num = list(map(int, sys.stdin.readline().split()))
flag = 0
temp = num[0]
for i in range(n):
    if num[i] != temp:
        flag = 1
        break
if flag == 0:
    print("{0} {1}".format(1, n))
else:
    l = 0
    r = 0
    al = 0
    ar = 0
    ans = 0
    now = 0
    for i in range(n):
        vis[num[i]] += 1
        if vis[num[i]] == 1:
            now += 1
        while now > m:
            vis[num[l]] -= 1
            if vis[num[l]] == 0:
                now -= 1
            l += 1
        if i - l + 1 > ar - al + 1:
            ar = i
            al = l
    print('{0} {1}'.format(al+1, ar+1))