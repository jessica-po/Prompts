n = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
A2 = [A[0]]
for a in A[1:]:
    A2.extend([a, a])
ans = 0
for a in A2[:n-1]:
    ans += a
print(ans)