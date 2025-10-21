n = int(input())
a = list(map(int,input().split()))
s = sum(a)
for k in range(max(a), 999999):
    vote = sum(k-x for x in a)
    if vote > s: print(k); break