from collections import Counter

n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

aidx = [-1]*n
bidx = [-1]*n

for i, (ai, bi) in enumerate(zip(a, b)):
    aidx[ai-1] = i
    bidx[bi-1] = i

diffs = [(aidx[i] - bidx[i]) % n for i in range(n)]
print(max(Counter(diffs).values()))