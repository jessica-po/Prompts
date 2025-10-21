n, k = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(k):
    c1 = c2 = 0
    for j in range(i, n, k):
        if A[j] == 1:
            c1 += 1
        else:
            c2 += 1
    ans += min(c1, c2)
print(ans)