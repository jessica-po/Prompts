n = int(input())
A = list(map(int, input().split()))

A.sort()
i = 0
j = 0
ans = 0

while j < len(A):
    ans = max(ans, j - i)
    if i == j or A[j] - A[i] <= 5:
        j += 1
    else:
        i += 1

print(max(ans, j - i))