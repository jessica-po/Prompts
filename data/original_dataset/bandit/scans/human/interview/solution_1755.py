import sys
from sys import stdin

import bisect

def LIS(lis , end):

    seq = []

    for c in lis:
        ind = bisect.bisect_right(seq,c)

        if ind == len(seq):
            seq.append(c)
        else:
            if ind != 0:
                seq[ind] = c

    return bisect.bisect_right(seq,end)

tt = 1

for loop in range(tt):

    n,k = list(map(int,stdin.readline().split()))
    a = list(map(int,stdin.readline().split()))
    b = list(map(int,stdin.readline().split()))

    a = [float("-inf")] + a + [float("inf")]
    b = [0] + b + [n+1]
    for i in range(n+2):
        a[i] -= i

    for i in range(len(b)-1):
        if a[b[i]] > a[b[i+1]]:
            print(-1)
            return

    ans = n+1
    for i in range(len(b)-1):
        now = LIS(a[ b[i]:b[i+1] ] , a[b[i+1]])
        ans -= now

    print (ans)