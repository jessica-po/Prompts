from collections import defaultdict
n = int(input())
A = [int(x) for x in input().split()]
D = defaultdict(int)
for a in A: D[a] += 1
S = set(D.keys())
ans = len(S) - 1
while S:
    for k in D:
        D[k] -= 1
        if D[k] <= 0 and k in S:
            S.remove(k)
    ans += len(S) - 1
print(ans + 1)