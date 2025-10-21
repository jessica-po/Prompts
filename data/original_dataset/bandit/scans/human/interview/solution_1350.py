from collections import Counter
n, k = list(map(int, input().split()))
c = Counter(input())
ans = min(c[chr(ord('A') + i)] for i in range(k))
print(k * ans)