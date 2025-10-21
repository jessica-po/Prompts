line = input().split()
n = int(line[0])
m = int(line[1])

W = [int(w) for w in input().split()]
B = [int(b) for b in input().split()]

ans = 0
lst = [0 for i in range(n)]
for i in range(m):
    arr = list(lst)
    for j in range(i):
        if B[i - j - 1] == B[i]:
            break
        arr[B[i - j - 1] - 1] = 1
    for i in range(n):
        if arr[i] == 1:
            ans += W[i]
print(ans)