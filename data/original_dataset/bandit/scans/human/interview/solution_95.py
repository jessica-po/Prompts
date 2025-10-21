n = int(input())
L = list(map(int, input().split()))
i = 0
a = 0
while i < n and L[i] > a:
    a = L[i]
    i += 1
while i < n and L[i] == a:
    i += 1
while i < n and L[i] < a:
    a = L[i]
    i += 1
if i == n:
    print("YES")
else:
    print("NO")