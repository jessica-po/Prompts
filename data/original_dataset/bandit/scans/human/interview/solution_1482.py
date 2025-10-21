#CF Round 150. Div II Prob. A - Dividing Orange
import sys

In = sys.stdin
n, k = [int(x) for x in In.readline().split()]
arr, s, cnt = [int(x) for x in In.readline().split()], set(), 1;
s.update(arr)
for i in range(k):
    c = [arr[i]]
    for j in range(n - 1):
        while (cnt in s):
            cnt += 1;
        c.append(cnt)
        cnt += 1;
    sep = ' '
    print (sep.join(map(str, c)))