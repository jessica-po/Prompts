from sys import stdin
from bisect import bisect_left
def read_bit(tree, idx):
    s = 0
    while idx > 0:
        s += tree[idx]
        idx -= (idx & -idx)
    return s
def update_bit(tree, idx, val):
    while idx < len(tree):
        tree[idx] += val
        idx += (idx & -idx)

n,t=list(map(int,stdin.readline().split()))
a=[int(x) for x in stdin.readline().split()]
pref=[0]*n
pref[0]=a[0]
for i in range(1,n):
    pref[i]=pref[i-1]+a[i]
pref.sort()
before=ans=0
tree=[0]*(n+2)
for i in range(n):
    ind = bisect_left(pref, t + before)
    if ind>0:
        ans += ind-read_bit(tree, ind)
    before += a[i]
    before_ind=bisect_left(pref, before)
    update_bit(tree, before_ind+1, 1)
print(ans)